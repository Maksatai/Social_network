from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
from autoslug import AutoSlugField

GENDER_CHOICES = [
    ['male', u"Мужской"],
    ['female', u"Женский"],
]

REL_CHOICES = [
    ['none', u"Не определенно"],
    ['single', u"Холост"],
    ['in_a_rel', u"В отношениях"],
    ['engaged', u"Помолвлен(а)"],
    ['married', u"Женат/Замужем"],
    ['in_love', u"Влюблен(а)"],
    ['complicated', u"Все сложно"],
]

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=u"Пользователь")
    avatar = models.FileField(verbose_name=u"Аватар", default='media/Profile.png', null=True, blank=True)
    bio = models.TextField(max_length=500, blank=True, null=True, verbose_name=u"О себе")
    city = models.CharField(max_length=30, blank=True, null=True, verbose_name=u"Город")
    birth_date = models.DateField(null=True, blank=True, verbose_name=u"Дата рождения")
    gender = models.CharField(max_length=10, verbose_name=u"Пол", choices=GENDER_CHOICES, default="male")
    relationship = models.CharField(max_length=20, verbose_name=u"Статус отношений", choices=REL_CHOICES, default="none")
    slug = AutoSlugField(populate_from='user')

    def __str__(self):
        return str(self.user.username)

    def get_absolute_url(self):
        return "/users/{}".format(self.slug)

# class Friend(models.Model):
#     class Meta:
#         db_table = 'Friend'
#     user = models.ForeignKey(User)
#     friends = models.ManyToManyField("self", blank=True)
#     date = models.DateTimeField(auto_now_add=True)

# from django.db import models
# from django.contrib.auth.models import User
# from django.utils import timezone
# from django.utils.translation import ugettext_lazy as _
 
 
# class Chat(models.Model):
#     DIALOG = 'D'
#     CHAT = 'C'
#     CHAT_TYPE_CHOICES = (
#         (DIALOG, _('Dialog')),
#         (CHAT, _('Chat'))
#     )
 
#     type = models.CharField(
#         _('Тип'),
#         max_length=1,
#         choices=CHAT_TYPE_CHOICES,
#         default=DIALOG
#     )
#     members = models.ManyToManyField(User, verbose_name=_("Участник"))
 
#     @models.permalink
#     def get_absolute_url(self):
#         return 'users:messages', (), {'chat_id': self.pk }
 
 
# class Message(models.Model):
#     chat = models.ForeignKey(Chat, verbose_name=_("Чат"))
#     author = models.ForeignKey(User, verbose_name=_("Пользователь"))
#     message = models.TextField(_("Сообщение"))
#     pub_date = models.DateTimeField(_('Дата сообщения'), default=timezone.now)
#     is_readed = models.BooleanField(_('Прочитано'), default=False)
 
#     class Meta:
#         ordering=['pub_date']
 
#     def __str__(self):
#         return self.message

