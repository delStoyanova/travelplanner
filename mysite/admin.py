from django.contrib import admin

from .models import TodoList, ProfileUser, Places, Post

# Register your models here.


admin.site.register(TodoList)
admin.site.register(ProfileUser)
admin.site.register(Places)
admin.site.register(Post)
