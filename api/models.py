from django.db import models
from django.contrib.auth.models import AbstractUser


class Job(models.Model):
    Role = models.CharField(max_length=20)
    JobDescription = models.CharField(max_length=200)
    CompanyName = models.CharField(max_length=20)
    Location = models.CharField(max_length=40)
    CTC = models.IntegerField()

    def __str__(self) -> str:
        return f"{self.Role} : {self.CompanyName}"


class Candidate(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email_id = models.CharField(max_length=50)
    DOB = models.DateField(blank=True, null=True)
    jobs = models.ManyToManyField(
        Job, related_name="Candidate_jobs", blank=True)
    phone_no = models.CharField(max_length=12, blank = True, null = True)
    current_role = models.CharField(max_length=20)
    current_ctc = models.IntegerField()
    experience = models.IntegerField()
    status_choices = [
        ("cv_surfaced", "CV Surfaced"),
        ("round_1", "Round 1"),
        ("round_2", "Round 2"),
        ("round_3", "Round 3"),
        ("offered", "Offered"),
        ("candidate_backed", "Candidate Backed"),
        ("offer_dropped", "Offer Dropped"),
        ("hr_reject","HR reject"),
        ("reject","Reject"),
        ("not_a_fit","Not a fit"),
        ("offer_negotiation","Offer Negotiation")
    ]
    status = models.CharField(
        max_length=30,
        choices=status_choices,
        default="CV surfaced",
    )

    def __str__(self) -> str:
        return f"{self.first_name}"


class User(AbstractUser):
    user_role_choices = [
        ("supervisior", "Supervisior"),
        ("hr", "HR")
    ]
    user_role = models.CharField(
        max_length=20,
        choices=user_role_choices,
        default="hr",
    )
    candidates = models.ManyToManyField(
        Candidate, related_name="User_candidates", blank=True)
    jobs = models.ManyToManyField(Job, related_name="User_jobs", blank=True)

    def _str_(self):
        return f"{self.username} : {self.user_role}"

class Mandate(models.Model):
    company_name = models.CharField(max_length=20)
    requirement = models.CharField(max_length=20)
    role_name = models.CharField(max_length=50)
    user = models.ForeignKey(User, related_name="mandates", on_delete=models.CASCADE, null=True, blank=True)  

    def __str__(self) -> str:
        return f"{self.company_name}"