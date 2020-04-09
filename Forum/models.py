from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Publication(models.Model):
    CHOICES = (
        ('Sport', 'Sport'),
        ('Science', 'Science'),
        ('Art', 'Art')
    )
    Title = models.CharField(max_length=200)
    Content = models.TextField()
    Likes = models.IntegerField(default=0)
    Dislikes = models.IntegerField(default=0)
    Resolved = models.BooleanField(default=False)
    Pub_User = models.ForeignKey(User, on_delete=models.CASCADE)
    Theme = models.CharField(max_length=20, choices=CHOICES)
    Pub_Date = models.DateTimeField(auto_now_add=True)
    Last_Modif = models.DateTimeField(auto_now =True)


class Comment(models.Model):
    Content = models.TextField()
    Subject_Id = models.PositiveIntegerField()
    isSatisfying = models.BooleanField(default=False)
    Comment_User = models.ForeignKey(User, on_delete=models.CASCADE)