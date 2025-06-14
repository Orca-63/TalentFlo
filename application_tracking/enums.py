from django.db import models

EmploymentType = [
    ("Full Time", "Full Time"),
    ("Internship", "Internship"),
    ("Freelance", "Freelance"),
    ("Contractual", "Contractual")
]


ExperienceLevel = [
    ("Fresher", "Fresher"),
    ("Junior", "Junior"),
    ("Mid Level", "Mid Level"),
    ("Senior", "Senior"),
    ("Lead", "Lead")
]


LocationTypeChoice = [
    ("Onsite", "Onsite"),
    ("Hybrid", "Hybrid"),
    ("Remote", "Remote")

]


class ApplicationStatus(models.TextChoices):
    APPLIED = ("APPLIED", "APPLIED")
    REJECTED = ("REJECTED", "REJECTED")
    INTERVIEW = ("INTERVIEW", "INTERVIEW")
