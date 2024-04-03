from django.contrib.auth.models import AbstractUser
from django.db import models


class AppUser(AbstractUser):
    name = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class StressLevelRecord(models.Model):
    user = models.ForeignKey(AppUser, on_delete=models.CASCADE)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    bmi_category = models.CharField(max_length=20)
    phq1 = models.IntegerField()
    phq2 = models.IntegerField()
    phq3 = models.IntegerField()
    phq4 = models.IntegerField()
    phq5 = models.IntegerField()
    phq6 = models.IntegerField()
    phq7 = models.IntegerField()
    phq8 = models.IntegerField()
    phq9 = models.IntegerField()
    phq_score_total = models.IntegerField()
    is_suicide = models.CharField(max_length=10)
    stress_level = models.CharField(max_length=20)
    recommendations = models.TextField()
    created = models.DateField(auto_now_add=True)
