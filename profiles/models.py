from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import User

class Profile(models.Model):
    owner = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    friends = models.ManyToManyField('self', symmetrical=False)
    first_name = models.CharField(max_length=50, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    email = models.EmailField(max_length=255, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255, blank=True)
    bio = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_profile_qdjgyp'
    )

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f"{self.first_name}'s profile"


def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(owner=instance, email=instance.email)


post_save.connect(create_profile, sender=User)
