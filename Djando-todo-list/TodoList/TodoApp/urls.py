from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),   # protected dashboard
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),
    path('update_task_status/<int:task_id>/', views.update_task_status, name='update_task_status'),
    path('share/<int:task_id>/', views.share_task, name='share_task'),

]
