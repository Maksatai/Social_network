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

    def get_all_profiles(self, me):
        profiles = Profile.objects.all().exclude(user=me)
        return profiles


class Profile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=u"User")
    avatar = models.FileField(verbose_name=u"Avatar", default='1.jpg')
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name=u"Bio", default="no bio...")
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"City")
    birth_date = models.DateField(null=True, blank=True, verbose_name=u"Date of birth")
    gender = models.CharField(max_length=10, verbose_name=u"Gender", choices=GENDER_CHOICES, default="male")
    relationship = models.CharField(max_length=20, verbose_name=u"Relationships", choices=REL_CHOICES, default="none")
    slug = AutoSlugField(populate_from='user')
    friends = models.ManyToManyField(User, blank=True, related_name='friends1')

    objects = ProfileManager()


    def __str__(self):
        return str(self.user.username)


    def get_absolute_url(self):

        return "/users/{}".format(self.slug)


    # def add_friend(self,account):

    #     if not account in self.friends.all():
    #         self.friends.add(account)
    #         self.save


    # def remove_friend(self, account):

    #     if account in self.friends.all():
    #         self.friends.remove(account)


    # def unfriend(self, removee):

    #     remover_friends_list = self
    #     remover_friends_list.remove_friend(removee)
    #     friend_list = Profile.objects.get(user=removee)
    #     friend_list.remove_friend(self.user)

    # def is_mutual_friend(self,friend):

    #     if friend in self.friends.all():
    #         return True
    #     return False
        

class FriendRequest(models.Model):

    sender = models.ForeignKey(User,on_delete=models.CASCADE, related_name="sender")
    receiver = models.ForeignKey(User,on_delete=models.CASCADE, related_name="receiver")
    is_active = models.BooleanField(blank=True, null=False, default = True)

    def __str__(self):
        return self.sender.username


    # def accept(self):

    #     receiver_friend_list = FriendRequest.objects.get(user=self.receiver)
    #     if receiver_friend_list:
    #         receiver_friend_list.add_friend(self.sender)
    #         sender_friend_list = FriendRequest.objects.get(user=self.sender)
    #         if sender_friend_list:
    #             sender_friend_list.add_friend(self.receiver)
    #             self.is_active = False
    #             self.save()

    # def decline(self):

    #     self.is_active = False
    #     self.save()

    # def cancel(self):

    #     self.is_active = False
    #     self.save()

        


        