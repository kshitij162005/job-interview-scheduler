from django import forms
from .models import Applicant, InterviewSlot, Assignment

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
        fields = '__all__'
