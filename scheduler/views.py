from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Applicant, InterviewSlot, Assignment
from .forms import AssignmentForm, ApplicantForm


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
            
            # Check if the interview slot is already assigned
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
    
    # Filters
    applicant_name = request.GET.get('applicant')
    status = request.GET.get('status')
    job_role = request.GET.get('job_role')

    if applicant_name:
        assignments = assignments.filter(applicant__name__icontains=applicant_name)
    if status:
        assignments = assignments.filter(interview_slot__status=status)
    if job_role:
        assignments = assignments.filter(interview_slot__job_role__icontains=job_role)

    return render(request, 'assignment_list.html', {
        'assignments': assignments,
        'filters': {
            'applicant': applicant_name or '',
            'status': status or '',
            'job_role': job_role or '',
        }
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
        return redirect('assignment_list')  # Ensure this points to the correct URL name
    
    # Check if the new status is available in the choices
    if request.method == 'POST':
        new_status = request.POST.get('status')

        if new_status in dict(InterviewSlot.STATUS_CHOICES).keys():
            interview_slot.status = new_status
            interview_slot.save()
            messages.success(request, 'Interview status updated successfully.')
        else:
            messages.error(request, 'Invalid status.')

        return redirect('assignment_list')  # Ensure this points to the correct URL name

    return render(request, 'update_status.html', {'interview_slot': interview_slot})
