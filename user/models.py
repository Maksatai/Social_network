from django.db import models
from django.db.models import Q
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

class ProfileManager(models.Manager):

    def get_all_profiles_to_invite(self, sender):
        profiles = Profile.objects.all().exclude(user=sender)
        profile = Profile.objects.get(user=sender)
        qs = Relationship.objects.filter(Q(sender=profile) | Q(receiver=profile))

        accepted = set([])
        for rel in qs:
            if rel.status == 'accepted':
                accepted.add(rel.receiver)
                accepted.add(rel.sender)
        
        available = [profile for profile in profiles if profile not in accepted]
        return available


    def get_all_profiles(self, me):
        profiles = Profile.objects.all().exclude(user=me)
        return profiles

    def get_friends(self, me):
        qs = Profile.objects.filter(friends__pk=me.pk)
        return qs


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=u"User")
    avatar = models.FileField(verbose_name=u"Avatar", default='1.jpg')
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name=u"Bio", default="no bio...")
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"City")
    birth_date = models.DateField(null=True, blank=True, verbose_name=u"Date of birth")
    gender = models.CharField(max_length=10, verbose_name=u"Gender", choices=GENDER_CHOICES, default="male")
    relationship = models.CharField(max_length=20, verbose_name=u"Relationships", choices=REL_CHOICES, default="none")
    slug = AutoSlugField(populate_from='user')
    friends = models.ManyToManyField(User, blank=True, related_name='friends')

    objects = ProfileManager()


    def __str__(self):
        return str(self.user.username)


    def get_absolute_url(self):

        return "/users/{}".format(self.slug)

    

    def get_likes_given_no(self):
        likes = self.likes1.all()
        total_liked = 0
        for item in likes:
            if item.value=='Like':
                total_liked +=1
        return total_liked

    def get_likes_recieved_no(self):
        posts = self.user_set.all()
        total_liked = 0
        for item in posts:
            total_liked += item.likes.all().count()
        return total_liked


STATUS_CHOICES = (
    ('send','send'),
    ('accepted','accepted'),
    ('remove','remove'),
)

class RelationshipManager(models.Manager):
    def invatations_received(self, receiver):
        qs = Relationship.objects.filter(receiver=receiver, status='send')
        return qs



class Relationship(models.Model):

    sender = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(Profile,on_delete=models.CASCADE, related_name="receiver")
    status = models.CharField(max_length=8,choices=STATUS_CHOICES)

    objects = RelationshipManager()

    def __str__(self):
        return str(self.sender.user)

        


        
