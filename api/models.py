from django.db import models
from django.utils import timezone

class Task(models.Model):
    task = models.CharField(max_length=150)
    task_detail = models.TextField(blank=True, null=True)
    date_posted = models.DateTimeField(default=timezone.now)
    schedule_date = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return 'Task: {}'.format(self.task)