from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from django.utils import timezone
from django.urls import reverse
from autoslug import AutoSlugField
from user.models import Profile

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='media/images', null=True, blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    tags = models.CharField(max_length=100, blank=True)
    likes = models.ManyToManyField(User, related_name='likes')

    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
        
    
  
    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

class Comment(models.Model):
	post = models.ForeignKey(Post, related_name='details', on_delete=models.CASCADE)
	username = models.ForeignKey(User, related_name='details', on_delete=models.CASCADE)
	comment = models.CharField(max_length=255)
	comment_date = models.DateTimeField(default=timezone.now)


LIKE_CHOICES = (
    ('Like','Like'),
    ('Unlike','Unlike'),
)

class Like(models.Model):
    user = models.ForeignKey(Profile, related_name='likes', on_delete=models.CASCADE)
    post = models.ForeignKey(Post, related_name='likes1', on_delete=models.CASCADE)
    # value = models.CharField(choices = LIKE_CHOICES, max_length = 8)

    def __str__(self):
        return f"{self.user}-{self.post}-{self.value}"


