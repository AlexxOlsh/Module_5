from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=15, blank=True, null=True)
    social_link = models.CharField(max_length=100, blank=True, null=True)
    github_id = models.CharField(max_length=255, blank=True, unique=True, null=True)

    # def clean(self):
    #     if self.github_id is None:
    #         raise ValidationError("Github_id must be set.")

    def __str__(self):
        return self.username


# class UserProfile(models.Model):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
