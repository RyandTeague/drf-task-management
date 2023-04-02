from django.contrib import admin
from django.contrib.auth.models import Group
admin.site.unregister(Group)


from .models import Group
admin.site.register(Group)
# Register your models here.
