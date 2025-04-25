from django.urls import path
from . import views

urlpatterns = [
    path('assign/', views.assign_interview, name='assign_interview'),
    path('assignments/', views.assignment_list, name='assignment_list'),
    path('add_applicant/', views.add_applicant, name='add_applicant'),
    path('applicants/', views.applicant_list, name='applicant_list'),
]
