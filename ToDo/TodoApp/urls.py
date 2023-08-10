from django.urls import path, include

from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('not-completed/', Not_Completed.as_view(), name='not_completed'),
    path('completed/', Completed.as_view(), name='completed'),
    path('delete/<int:task_id>', delete, name='delete'),
    path('complete/<int:task_id>', complete, name='complete'),
    path('add-task/', AddTask.as_view(), name='add_task'),
    path('edit/<int:task_id>', EditTask.as_view(), name='edit_task'),
    path('logout/', logout_user, name='logout'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    ]