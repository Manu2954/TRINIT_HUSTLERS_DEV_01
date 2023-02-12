from django.db import models
from django.contrib.auth.models import User
import uuid
import datetime

# Create your models here.

class Organisation(models.Model):
    ngo_name=models.CharField(max_length=1000,default="")
    email=models.CharField(max_length=1000,default='')
    description=models.CharField(max_length=5000,default="")
    is_ngo=models.BooleanField(default=False)
    goal=models.TextField(default="")
    location=models.CharField(default='',max_length=1000)
    ngo_type=models.CharField(default='',max_length=1000)

class Post(models.Model):
    id=models.UUIDField(primary_key=True,default=uuid.uuid4)
    user=models.CharField(max_length=1000,default='')
    caption=models.TextField(default='')
    image=models.ImageField(upload_to='img/%Y')
    description=models.TextField()
    created_at=models.DateTimeField(default=datetime.datetime.now)
    likes=models.IntegerField(default=0)

    def __str__(self):
        return self.user

class Philanthropist(models.Model):
    username = models.CharField(max_length=1000,default='')
    email=models.CharField(max_length=1000,default='')
    user_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
