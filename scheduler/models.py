from django.db import models

class Applicant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    job_applied_for = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class InterviewSlot(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    date = models.DateField()
    time = models.TimeField()
    interviewer_name = models.CharField(max_length=100)
    job_role = models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')

    def __str__(self):
        return f"{self.date} - {self.time} with {self.interviewer_name}"

class Assignment(models.Model):
    interview_slot = models.ForeignKey(InterviewSlot, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.applicant} assigned to {self.interview_slot}"
