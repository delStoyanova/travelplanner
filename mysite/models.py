from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone


# Create your models here.
# whenever you are changing the structure, you should migrate
# if you add another model or attribute to existing-migrate
# def function-no migration
# new model:makemigrations>migrate>sqlmigrate mysite 000#>migrate

class TodoList(models.Model):
    user = models.ForeignKey('auth.User')
    title = models.CharField(max_length=250, default="title")
    due_date = models.DateField(default=timezone.now)
    finished = models.DateField(blank=True, null=True)
    is_done = models.BooleanField(default=False)

    def finish(self):
        self.is_done = True
        self.finished = timezone.now()
        self.save()

    def __str__(self):
        return "Item is: " + self.title


class ProfileUser(models.Model):
    author = models.ForeignKey('auth.User')
    avatar = models.FileField(upload_to='avatars',default='none')

    # string representation of the object
    def __str__(self):
        return "Photo of:  " + self.author.username


class Places(models.Model):
    owner = models.ForeignKey('auth.User')
    name = models.CharField(max_length=250)

    def __str__(self):
        return "Name of place " + self.name


class Post(models.Model):
    person = models.ForeignKey('auth.User')
    text = models.TextField()
    published_date = models.DateField(default=timezone.now)

    def __str__(self):
        return "Post: " + self.text


"""


class Todolist(models.Model):
    user = models.ForeignKey('auth.User')
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=250)

    def __str__(self):
        return "To-dolist for : " + self.user_name + "made on: " + self.date


class Todolist(models.Model):
    user_name = models.CharField(max_length=100)
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.CharField(max_length=250)

    def __str__(self):
        return "To-dolist for : " + self.user_name + "made on: " + self.date


class Item(models.Model):
    todolist = models.ForeignKey(Todolist, on_delete=models.CASCADE)
    name = models.CharField(max_length=1000)
    is_done = models.BooleanField(default=False)

    def __str__(self):
        return "Item in todolist number : " + str(self.todolist.id) + " is " + self.name

class SavedArticles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='SOME STRING')


class Places(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='SOME STRING')


class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='SOME STRING')
    f_name = User.first_name
    l_nme = User.last_name
    context = models.CharField(max_length=10000)
"""
