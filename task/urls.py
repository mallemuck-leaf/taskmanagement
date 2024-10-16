from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('add_task/', views.edit_task, name='add_task'),
    path('', views.task_page, name='task_page'),
    path('detail/<int:pk>', views.task_detail, name='task_detail'),
    path('comment/<int:pk>', views.comment_detail, name='task_comment'),
]