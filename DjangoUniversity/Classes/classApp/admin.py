from django.contrib import admin

from .models import djangoClasses

admin.site.register(djangoClasses)  # registering the class in models.py so we can make changes to the database with in our website
