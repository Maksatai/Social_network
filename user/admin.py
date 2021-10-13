from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
from .models import Profile

admin.site.register(Profile)
# admin.site.register(User, UserAdmin)
