from django.db import models
from django.conf import settings
from django.contrib.auth.models import User


class Person(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        if self.user.first_name is not None and self.user.last_name is not None:
            return f'{self.user.first_name} {self.user.last_name}'
        if self.user.first_name is not None:
            return f'{self.user.first_name} -'
        if self.user.last_name is not None:
            return f'- {self.user.last_name}'
        return f'{self.user.username}'


class Status(models.TextChoices):
    INWAITING = 'w', 'в ожидании'
    INPROCESS = 'p', 'в процессе'
    COMPLETED = 'c', 'завершено'


class Task(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    executor = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='executing')
    customer = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='customering')
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.INWAITING)
    date_created = models.DateTimeField(auto_now_add=True)
    date_to_complete = models.DateField()


class Comment(models.Model):
    customer = models.ForeignKey('Person', on_delete=models.CASCADE, related_name='commenting')
    task = models.ForeignKey('Task', on_delete=models.CASCADE, related_name='task_commenting')
    content = models.TextField(max_length=1000)
    ex_content = models.TextField(max_length=1000, blank=True, null=True)

