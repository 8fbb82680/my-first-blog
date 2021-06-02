from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # models.ForeignKey – 他のモデルへのリンク
    title = models.CharField(max_length=200) # models.CharField - 文字数が制限されたテキストを定義するフィールド
    text = models.TextField() # models.TextField - 文字数の制限なしを定義するフィールド
    created_date = models.DateTimeField(default=timezone.now) # models.DateTimeField - 日付と時間のフィールド
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
