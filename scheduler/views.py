from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Applicant, InterviewSlot, Assignment
from .forms import AssignmentForm

from .forms import ApplicantForm, Applicant


def add_applicant(request):
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('applicant_list')  
    else:
        form = ApplicantForm()
    
    return render(request, 'add_applicant.html', {'form': form})

def assign_interview(request):
    if request.method == 'POST':
        form = AssignmentForm(request.POST)
        if form.is_valid():
            interview_slot = form.cleaned_data['interview_slot']
            applicant = form.cleaned_data['applicant']
            
            if Assignment.objects.filter(interview_slot=interview_slot).exists():
                messages.error(request, 'This interview slot is already assigned to another applicant.')
                return redirect('assign_interview')  
            
            form.save()
            messages.success(request, 'Interview successfully assigned to the applicant.')
            return redirect('assignment_list') 
    
    else:
        form = AssignmentForm()

    return render(request, 'assign_interview.html', {'form': form})

def assignment_list(request):
    assignments = Assignment.objects.select_related('applicant', 'interview_slot')
    return render(request, 'assignment_list.html', {'assignments': assignments})

def applicant_list(request):
    applicants = Applicant.objects.all()
    return render(request, 'applicant_list.html', {'applicants': applicants})

