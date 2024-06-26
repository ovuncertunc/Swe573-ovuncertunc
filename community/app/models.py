from django.db import models
from django.utils import timezone

class Community(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    privacy = models.CharField(max_length=10)
    owner = models.CharField(max_length=30)
    description = models.CharField(max_length=300)
    community_photo = models.ImageField(upload_to='community_picture/', default=None, null=True, blank=True)

class UserCommunityMembership(models.Model):
    objects = None
    username = models.CharField(max_length=30)
    community = models.CharField(max_length=100)
    joined_date = models.DateTimeField(default=timezone.now, editable=False)

class UserJoinInvitations(models.Model):
    objects = None
    username = models.CharField(max_length=30)
    community_name = models.CharField(max_length=100)
    is_suspended = models.BooleanField(default=False)

class Posts(models.Model):
    objects = None
    template_name = models.CharField(max_length=100)
    template_dict = models.JSONField()
    #photo = models.ImageField(upload_to='images')
    #location = models.FloatField()
    community_name = models.CharField(max_length=100)
    author_username = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)

class UserProfile(models.Model):
    objects = None
    username = models.CharField(max_length=100)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    birthdate = models.DateTimeField(null=True, blank=True)
    about_me = models.CharField(max_length=300, null=True, blank=True)
    profile_picture = models.ImageField(upload_to='images/', default=None, null=True, blank=True)

class CommunitySpecificTemplate(models.Model):
    objects = None
    community_name = models.CharField(max_length=100)
    template_name = models.CharField(max_length=300)
    template_dict = models.CharField(max_length=10000)