from django.contrib.auth.models import User
from django.db import models

class Tasks(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    title = models.TextField(max_length=255)
    content = models.TextField(max_length=255, blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    completed = models.BooleanField(default=0)
