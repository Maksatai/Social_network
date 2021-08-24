from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='will/create/later', null=True, blank=True)
    video = models.FileField(upload_to='will/create/later', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    tags = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'