from django.contrib import admin
from .models import Organisation, Philanthropist, Post
# Register your models here.

admin.site.register(Organisation)
admin.site.register(Philanthropist)
admin.site.register(Post)
