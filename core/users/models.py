from django.db import models
from django.contrib.auth.models import AbstractUser
from .enums import *


class User(AbstractUser):
    photo = models.ImageField(upload_to='users/photo/', blank=True)
    resume = models.FileField(upload_to='users/resumes/', blank=True)
    age = models.PositiveIntegerField(blank=False)
    job_status = models.CharField(
        max_length=200, choices=JobStatus.choices(), default=JobStatus.CHECKING)
    marital_status = models.CharField(
        max_length=200, choices=MaritalStatus.choices(), default=MaritalStatus.NO_ANSWER)
    gender = models.CharField(
        max_length=200, choices=Gender.choices(), default=Gender.NO_ANSWER)
