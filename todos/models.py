from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

"""
class Project(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    deadline = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.id} {self.title}'
"""


class Todo(models.Model):
    deadline = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
#    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='todos', null=True)


    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.id} {self.title}'