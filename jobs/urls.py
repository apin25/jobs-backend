from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns=[
    path('add-job',add_job),
    path('get-list-job',get_list_job),
    path('update-job/<str:id>',update_job),
    path('get-job-detail/<str:id>',get_job_detail),
    path('delete-job/<str:id>', delete_job)
]