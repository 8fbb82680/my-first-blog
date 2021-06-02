from django.contrib import admin
from .models import Post # models.pyで作成したPostをimport

admin.site.register(Post)
