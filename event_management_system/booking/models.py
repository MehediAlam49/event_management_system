from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class EventUserModel(AbstractUser):
    full_name = models.CharField(max_length=100, null=True,blank=True)
    phone_number = models.CharField(max_length=20, null=True,blank=True)
    profile_image = models.ImageField(upload_to='media/profile-images', null=True,blank=True)

class EventBookingModel(models.Model):
    event_title = models.CharField(max_length=100, null=True, blank=True)
    event_type = models.CharField(choices=[('Conference','Conference'), ('concert','concert'), ('Weeding','Weeding')], null=True, blank=True)
    event_description = models.TextField(null=True, blank=True)
    event_date = models.DateField(null=True, blank=True)
    status = models.CharField(choices=[('NotStarted','NotStarted'), ('InProgress','InProgress'), ('completed','completed')], null=True, blank=True)
    location = models.CharField(max_length=100, null=True, blank=True)
    created_by = models.ForeignKey(EventUserModel, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True,blank=True)
    updated_at = models.DateTimeField(auto_now=True, null=True,blank=True)