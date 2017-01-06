from django import forms
from  django.contrib.auth.models import User

from .models import TodoList, Places, Post


# generic user class that we can use

# what to display on the register form
class UserForm(forms.ModelForm):
    ## hide what the user is typing with *
    password = forms.CharField(widget=forms.PasswordInput)

    # information about the class
    class Meta:
        # whenever a user makes registration, it goes to table User
        model = User
        # what fields are going to appear
        fields = ['username', 'email', 'password', 'first_name', 'last_name']


class UpdateUserForm(forms.ModelForm):
    # information about the class
    class Meta:
        # whenever a user makes registration, it goes to table User
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']


# what to display on the list form
class ListForm(forms.ModelForm):
    # information about the class
    class Meta:
        model = TodoList
        fields = ['title', 'due_date', 'is_done']


# what to display on the places form
class PlaceForm(forms.ModelForm):
    # information about the class
    class Meta:
        model = Places
        fields = ['name']

class PostForm(forms.ModelForm):
    # information about the class
    class Meta:
        model = Post
        fields = ['text']

class DocumentForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
    )
