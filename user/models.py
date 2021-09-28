from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from autoslug import AutoSlugField

GENDER_CHOICES = [
    ['male', u"Man"],
    ['female', u"Woman"],
]

REL_CHOICES = [
    ['none', u"Undefined"],
    ['single', u"Single"],
    ['in_a_rel', u"In relationships"],
    ['engaged', u"Engaged"],
    ['married', u"Married"],
    ['in_love', u"in love"],
    ['complicated', u"Complicated"],
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=u"User")
    avatar = models.FileField(verbose_name=u"Avatar", default='media/Profile.png', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name=u"Bio")
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"City")
    birth_date = models.DateField(null=True, blank=True, verbose_name=u"Date of birth")
    gender = models.CharField(max_length=10, verbose_name=u"Gender", choices=GENDER_CHOICES, default="male")
    relationship = models.CharField(max_length=20, verbose_name=u"Relationships", choices=REL_CHOICES, default="none")
    slug = AutoSlugField(populate_from='user')
    friends = models.ManyToManyField("Profile", blank=True)

    def __str__(self):
        return str(self.user.username)

    def get_absolute_url(self):
        return "/users/{}".format(self.slug)



class FriendRequest(models.Model):
	to_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='to_user', on_delete=models.CASCADE)
	from_user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='from_user', on_delete=models.CASCADE)
	timestamp = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return "From {}, to {}".format(self.from_user.username, self.to_user.username)