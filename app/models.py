from django.db import models
from django.urls import reverse
from django.conf import settings

class UserProfiles(models.Model):
  user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE, null=True, blank=True)
  fullname = models.CharField(max_length=224, null=True, blank=True)
  email = models.CharField(max_length=254, null=True, blank=True)
  phone = models.CharField(max_length=254, null=True, blank=True)
  avatar = models.FileField(upload_to ='uploads/', null=True, blank=True)
  comments = models.TextField(max_length=254, null=True, blank=True)
  created = models.DateTimeField(auto_now_add=True)
  updated = models.DateTimeField(auto_now=True)

  def __unicode__(self):
    return self.user
