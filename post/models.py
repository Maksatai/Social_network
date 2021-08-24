from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

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

    # def get_absolute_url(self):
	# 	return reverse('post-detail', kwargs={'pk': self.pk})
  
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'


class Like(models.Model):
	user = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
	post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)