from django.contrib import admin

from .models import *

# Register your models here.
class TasksAdmin(admin.ModelAdmin):
    list_display = ('id', "user", 'title', "content", "time_create", "time_update", "completed")

admin.site.register(Tasks, TasksAdmin)