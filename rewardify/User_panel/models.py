from django.db import models
from Admin_panel.models import App

class User_profile(models.Model):
    name = models.CharField(max_length=255)
    email_id = models.EmailField()
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)
    points_earned = models.IntegerField(default=0)

class Task(models.Model):
    user = models.ForeignKey(User_profile, on_delete=models.CASCADE)
    app = models.ForeignKey(App, on_delete=models.CASCADE)
    screenshot = models.ImageField(upload_to='screenshots/')
    points_earned = models.IntegerField(default=0)
