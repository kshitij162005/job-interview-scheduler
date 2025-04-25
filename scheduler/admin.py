from django.contrib import admin
from .models import Applicant, InterviewSlot, Assignment

admin.site.register(Applicant)
admin.site.register(InterviewSlot)
admin.site.register(Assignment)
