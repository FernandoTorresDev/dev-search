from users.models import Message, Profile, Skill
from django.contrib import admin

# Register your models here.
admin.site.register(Profile)
admin.site.register(Skill)
admin.site.register(Message)
