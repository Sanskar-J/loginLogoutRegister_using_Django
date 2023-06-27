from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class CustomUser(models.Model):
    id = models.AutoField(primary_key=True)
    phone_number = models.CharField(
        max_length=150,
        unique=True,
        help_text="Required. 150 characters or fewer. Unique phone number.",
        error_messages={
            'unique': "A user with that phone number already exists.",
        },
    )
    password = models.CharField(max_length=128)
    email=models.CharField(blank=True, max_length=100)