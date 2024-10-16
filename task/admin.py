from django.contrib import admin
from .models import Person, Task, Comment


@admin.register(Person)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['user',]


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['title', 'description', 'executor', 'customer', 'status', 'date_to_complete']
    list_filter = ['executor', 'customer', 'status']


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['task', 'customer', 'content', 'ex_content']
    list_filter = ['task', 'customer']
