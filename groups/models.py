from django.db import models
from django.contrib.auth.models import User


class Group(models.Model):
    owner = models.ForeignKey(
        User, related_name='group_created', on_delete=models.CASCADE
    )
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='group_member')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f'{self.owner} {self.name}'

