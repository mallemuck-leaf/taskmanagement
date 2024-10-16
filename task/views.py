from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Person, Task, Comment
from .forms import TaskEditForm, StatusUpdateForm, CommentEditForm


@login_required
def edit_task(request):
    if request.method == 'POST':
        form = TaskEditForm(data=request.POST)
        if form.is_valid():
            new_task = form.save(commit=False)
            new_task.customer = Person.objects.get(id=request.user.id)
            new_task.save()
            messages.success(request, 'Задача успешно добавлена')
        else:
            messages.error(request, 'Что-то пошло не так.')
    else:
        form = TaskEditForm()
    return render(request, 'task/add_task.html', {'task_edit_form': form})


@login_required
def task_detail(request, pk):
    if request.method == 'POST':
        form = StatusUpdateForm(data=request.POST)
        if form.is_valid():
            updated_task = form.save(commit=False)
            Task.objects.filter(id=pk).update(status=updated_task.status)
            content = {
                'tasks': Task.objects.filter(id=pk),
                'form': form,
            }
            return render(request, 'task/task_detail.html', content)
    form = StatusUpdateForm()
    content = {
        'tasks': Task.objects.filter(id=pk),
        'form': form,
    }
    return render(request, 'task/task_detail.html', content)


@login_required
def task_page(request):
    content = {
        'tasks': Task.objects.order_by('-date_created'),
    }
    return render(request, 'task/task_list.html', content)


@login_required
def comment_detail(request, pk):
    if request.method == 'POST':
        comment_form = CommentEditForm(data=request.POST)
        [print(x) for x in request.POST]
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.customer = Person.objects.get(user=request.user)
            new_comment.task = Task.objects.get(id=pk)
            new_comment.save()
            messages.success(request, 'Задача успешно добавлена')
        else:
            messages.error(request, 'Что-то пошло не так.')

    comment_form = CommentEditForm()
    task_object = Task.objects.get(id=pk)
    comments = Comment.objects.filter(task=task_object)
    content = {
        'comments': comments,
        'form': comment_form,
        'index': pk,
        'task': task_object,
    }
    return render(request, 'task/task_comments.html', content)
