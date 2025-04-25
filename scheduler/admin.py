from django.contrib import admin
from .models import Applicant, InterviewSlot, Assignment

@admin.register(Applicant)
class ApplicantAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'job_applied_for')  # Display ID
    search_fields = ('name', 'email', 'job_applied_for')

@admin.register(InterviewSlot)
class InterviewSlotAdmin(admin.ModelAdmin):
    list_display = ('id', 'date', 'time', 'interviewer_name', 'job_role', 'status')  # Display ID
    list_filter = ('status', 'job_role', 'date')
    search_fields = ('interviewer_name', 'job_role')

@admin.register(Assignment)
class AssignmentAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'interview_slot')  # Display applicant and interview slot
    search_fields = ('applicant__name', 'interview_slot__interviewer_name')

