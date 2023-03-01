from django.contrib import admin
from .models import User
from django.utils.safestring import mark_safe
# Register your models here.

admin.site.register(User)