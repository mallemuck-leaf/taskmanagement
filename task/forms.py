from django import forms
from .models import Person, Task, Comment, Status


class TaskEditForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'executor', 'date_to_complete']


class StatusUpdateForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['status',]


class CommentEditForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content',]
