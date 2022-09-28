from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('login/', views.login, name='login'),
    path('new-process/', views.new_process, name='new-process'),
    path('process-execution/', views.process_execution, name='process-execution'),
    path('project-management/', views.project_management, name='project-management'),
    path('user-management/', views.user_management, name='user-management'),
    path('role-management/', views.role_management, name='role-management'),
    path('job-dashboard/', views.job_dashboard, name='job-dashboard'),
    path('template-details/', views.template_details, name='template-details'),
    path('template-configuration/', views.template_configuration, name='template-configuration'),
    path('notification-config/', views.notification_config, name='notification-config'),
    path('schedule-project/<str:pk>', views.schedule_project, name='schedule-project'),
    path('delete_process/<str:pk>', views.delete_process, name='delete_process'),
    path('update_task/<str:pk>', views.update_task, name='update_task'),
    path('scheduled-task/', views.schedules_task, name='scheduled_task'),
]
