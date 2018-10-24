from django.contrib import admin
from .models import Website,Article,ArticlePicture
# Register your models here.
admin.site.register(Website)
admin.site.register(Article)
admin.site.register(ArticlePicture)