from django import forms
from .models import Assignment, InterviewSlot, Applicant

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = ['name', 'email', 'job_applied_for']

class ApplicantForm(forms.ModelForm):
    class Meta:
        model = Applicant
        fields = '__all__'

class InterviewSlotForm(forms.ModelForm):
    class Meta:
        model = InterviewSlot
        fields = '__all__'

class AssignmentForm(forms.ModelForm):
    class Meta:
        model = Assignment
        fields = ['interview_slot', 'applicant']
