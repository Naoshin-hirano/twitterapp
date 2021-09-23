from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class TweetPost(models.Model):
    content = models.TextField(verbose_name="本文")
    image = models.ImageField(upload_to="user_", blank=True, verbose_name="ツイートのイメージ写真", help_text="登録しない場合は、デフォルトのイメージ写真を使用する")
    liked = models.IntegerField(default=0, verbose_name="いいね数")
    creator = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="投稿日時")
    modified_at = models.DateTimeField(auto_now=True, verbose_name="更新日")

    def __str__(self):
        return self.content