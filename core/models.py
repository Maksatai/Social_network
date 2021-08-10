from django.db import models

# Create your models here.

class User(models.Model):
    login = models.ForeignKey(to=User, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    age = models.IntegerField(max=100, min=10)      
    email = models.CharField(max_length=255)
    decription = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    friends = models.IntegerField(default=0)
    is_online = models.BooleanField(default=False)

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['name']