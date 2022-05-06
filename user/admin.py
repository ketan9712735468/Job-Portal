from django.contrib import admin

from user.models import Category, Job, Profile

# Register your models here.

admin.site.register(Profile)
admin.site.register(Job)
admin.site.register(Category)