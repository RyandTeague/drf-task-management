from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class Todo(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_tasks', default=1)
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=100)
    deadline = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    assigned_to = models.ForeignKey(User, on_delete=models.CASCADE, related_name='assigned_tasks', default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    overdue = models.BooleanField(default=False)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'

    def save(self, *args, **kwargs):
        if self.deadline and datetime.now() > self.deadline:
            self.overdue = True
        else:
            self.overdue = False
        super(Todo, self).save(*args, **kwargs)
