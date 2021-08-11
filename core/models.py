from django.db import models

# Create your models here.

class Post(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    text = models.TextField(null=True, blank=True)
    photo = models.ImageField(null=True, blank=True)
    video = models.FileField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
        ordering = ['created_at']