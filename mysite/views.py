from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View

from .forms import UserForm, ListForm, UpdateUserForm, PlaceForm, PostForm, DocumentForm
from .models import User, TodoList, Places, Post, ProfileUser


# Create your views here.
# change profile settings
@login_required
@transaction.atomic
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            user_form = UpdateUserForm(instance=request.user)
            message = {'message': 'Your profile was successfully updated!', 'user_form': user_form, }
            return render(request, 'profile.html', message)
        else:
            message = {'message': 'Error'}
            return render(request, 'profile.html', message)
    if request.method == "GET":
        prof = ProfileUser.objects.all()
        user_form = UpdateUserForm(request.POST, instance=request.user)
        return render(request, 'profile.html', {
            "prof": prof,'user_form': user_form, })
    else:
        # image = prof.avatar
        user_form = UpdateUserForm(instance=request.user)
    return render(request, 'profile.html', {
        'user_form': user_form, })


##add item to ToDolist for the specific logged in user
class ListFormView(View):
    form_class = ListForm
    template_name = 'todo.html'

    # show the items already saved on the server
    def get(self, request):
        items = TodoList.objects.filter(user=request.user)
        return render(request, self.template_name, {'items': items})

    def post(self, request):
        # when user press the add button
        form = self.form_class(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            title = form.cleaned_data['title']
            date = form.cleaned_data['due_date']
            ##date=form.cleaned_data['date']
            # user = User.objects.get(id=user_id)
            current_user = request.user
            item = TodoList()
            item.title = title
            item.user = current_user
            item.due_date = date
            item.save()
            items = TodoList.objects.filter(user=request.user).order_by('due_date')
            return render(request, self.template_name, {'items': items})


# make an item finished from the list
def finishitem(request, item_id):
    finish_item = TodoList.objects.get(pk=item_id)
    finish_item.finish()
    deleted = {'deleted': "You successfully marked that item as finished", }
    return render(request, 'todo.html', deleted)


# delete one specific item from todolist
def deleteitem(request, item_id):
    delete_item = TodoList.objects.get(pk=item_id)
    delete_item.delete()
    deleted = {'deleted': "You successfully deleted that item", }
    return render(request, 'todo.html', deleted)


# delete all items of one user
def deleteall(request):
    items = TodoList.objects.filter(user=request.user)
    items.delete()
    deleted = {'deleted': "You successfully deleted all items", }
    return render(request, 'todo.html', deleted)


# registration of user, and logged in after that
class UserFormView(View):
    # whats the blueprint we already created
    form_class = UserForm
    # specify the template
    template_name = 'register.html'

    # display blank form, for user to fill data
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # when user press register button
    def post(self, request):
        form = self.form_class(request.POST)
        # django checks if it is valid
        if form.is_valid():
            # creates an object of user but havent submit it because it is checked again
            user = form.save(commit=False)
            # the information is put in some format
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            email = form.cleaned_data['email']
            first = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            user.first_name = first
            user.last_name = last_name
            user.email = email
            # the password appear with an algorithm in django
            user.set_password(password)
            # user is saved to database
            user.save()

            # user is authenticated in the database and logged in
            user = authenticate(username=username, password=password)
            # the user is found
            if user is not None:
                # the user is real
                if user.is_active:
                    login(request, user)
                    # redirect to homepage
                    return redirect('mysite:home')
                    # request.username show username
        # try again to login
        return render(request, self.template_name, {'form': form})


##user login
class UserLogin(View):
    # specify the template
    template_name = 'login.html'
    form_class = UserForm

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        # the information is put in some format
        username = request.POST['username1']
        password = request.POST['password1']

        # user is authenticated in the database and logged in
        user = authenticate(username=username, password=password)
        # the user is found
        if user is not None:
            # the user is real
            if user.is_active:
                login(request, user)
                # redirect to homepage
                # return redirect('mysite:home')
                message = {'message': 'Logged in successfully.', }
                return render(request, 'index.html', message)

                # return render(request, 'index.html', {'username': username})
                # request.username show username

        else:
            # try again to login
            errors = {'errors': 'Your password and/or username is wrong, please try again.', }
            return render(request, 'login.html', errors)


##user logout
def user_logout(request):
    logout(request)
    form = UserForm(request or None)

    # context = {"form": form, }
    # return render(request, 'login.html', context)
    message = {'message': 'Logged out successfully.', }
    return render(request, 'index.html', message)
    # return redirect('mysite:home')


# write a post with author the logged in user
class PostFormView(View):
    form_class = PostForm
    template_name = 'share.html'

    # show the items already saved on the server
    def get(self, request):
        items = Post.objects.all().order_by('published_date')
        prof = ProfileUser.objects.all()
        return render(request, self.template_name, {'items': items,'prof': prof})

    def post(self, request):
        # when user press the add button
        form = self.form_class(request.POST)
        if form.is_valid():
            exp = form.cleaned_data['text']
            current_user = request.user
            item = Post()
            item.person = current_user
            item.text = exp
            item.save()
            items = Post.objects.all().order_by('published_date')
            prof = ProfileUser.objects.all()
            return render(request, self.template_name, {'prof': prof})
        else:
            message = {'message': 'Error'}
            return render(request, self.template_name, message)


# delete specific post of logged in user
def deletepost(request, post_id):
    delete_post = Post.objects.get(pk=post_id)
    delete_post.delete()
    deleted = {'deleted': "You successfully deleted your post", }
    return render(request, 'share.html', deleted)


## save a specific place
class PlacesFormView(View):
    form_class = PlaceForm
    template_name = 'places.html'

    # show the items already saved on the server
    def get(self, request):
        items = Places.objects.filter(owner=request.user)
        return render(request, self.template_name, {'items': items})

    def post(self, request):
        # when user press the add button
        form = self.form_class(request.POST)
        if form.is_valid():
            item = form.save(commit=False)
            name = form.cleaned_data['name']
            current_user = request.user
            item = Places()
            item.owner = current_user
            item.name = name
            item.save()
            items = Places.objects.filter(owner=request.user)
            return render(request, self.template_name, {'items': items})
        else:
            message = {'message': 'Error'}
            return render(request, 'profile.html', message)

            # delete one specific item


# put the name of the place list in google maps
def findplace(request, place_id):
    item_place = Places.objects.get(pk=place_id)
    name = item_place.name
    message_text = {'message_text': "Your place is found.", "name": name, }
    return render(request, 'places.html', message_text)


# delete the place from the list
def deleteplace(request, place_id):
    item_place = Places.objects.get(pk=place_id)
    item_place.delete()
    items = Places.objects.filter(owner=request.user)
    message_text = {'message_text': "Your place is deleted.", 'items': items}
    return render(request, 'places.html', message_text)


def home(request):
    return render(request, 'index.html')


def places(request):
    return render(request, 'places.html')


def share(request):
    return render(request, 'share.html')


def register(request):
    return render(request, 'register.html')


def pack(request):
    return render(request, 'pack.html')


def guides(request):
    return render(request, 'guides.html')


def attractive_places(request):
    return render(request, 'attractive.places.html')


def advices(request):
    return render(request, 'advices.html')


# detail about the user,if it doesnt find it 404
def detail(request, user_id):
    user = get_object_or_404(User, pk=user_id)
    return render(request, 'index.html', {"user": user})


def photo(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = ProfileUser(avatar=request.FILES['docfile'])
            newdoc.author = request.user
            newdoc.save()

            return render(request, 'profile.html', {'message': "Photo uploaded"})
    else:
        form = DocumentForm()  # A empty, unbound form

    # Render list page with the documents and the form
    return render(request, 'profile.html', {'form': form})
