from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Applicant, InterviewSlot, Assignment
from .forms import AssignmentForm, ApplicantForm
from django.db.models import Q
from datetime import datetime


def add_applicant(request):
    """View to handle adding new applicants."""
    if request.method == 'POST':
        form = ApplicantForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Applicant added successfully.')
            return redirect('applicant_list')  
    else:
        form = ApplicantForm()
    
    return render(request, 'add_applicant.html', {'form': form})


def assign_interview(request):
    """View to handle assigning an interview to an applicant."""
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
    status_filter = request.GET.get('status')
    date_filter = request.GET.get('date')

    assignments = Assignment.objects.select_related('applicant', 'interview_slot')

    if status_filter:
        assignments = assignments.filter(interview_slot__status=status_filter)

    if date_filter:
        try:
            date_obj = datetime.strptime(date_filter, "%Y-%m-%d").date()
            assignments = assignments.filter(interview_slot__date=date_obj)
        except ValueError:
            pass  # ignore invalid date format

    statuses = InterviewSlot.STATUS_CHOICES
    return render(request, 'assignment_list.html', {
        'assignments': assignments,
        'statuses': statuses,
        'selected_status': status_filter,
        'selected_date': date_filter,
    })


def applicant_list(request):
    """View to list all applicants."""
    applicants = Applicant.objects.all()
    return render(request, 'applicant_list.html', {'applicants': applicants})


def update_status(request, slot_id):
    try:
        interview_slot = InterviewSlot.objects.get(id=slot_id)
    except InterviewSlot.DoesNotExist:
        messages.error(request, "The requested interview slot does not exist.")
        return redirect('assignment_list')  
    
    if request.method == 'POST':
        new_status = request.POST.get('status')

        if new_status in dict(InterviewSlot.STATUS_CHOICES).keys():
            interview_slot.status = new_status
            interview_slot.save()
            messages.success(request, 'Interview status updated successfully.')
        else:
            messages.error(request, 'Invalid status.')

        return redirect('assignment_list') 

    return render(request, 'update_status.html', {'interview_slot': interview_slot})

def assignments_view(request):
    assignments = Assignment.objects.all()
    return render(request, 'assignments.html', {'assignments': assignments})


def home(request):
    return render(request, 'home.html')

