# Generated by Django 3.2.6 on 2021-09-23 05:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TweetPost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField(verbose_name='本文')),
                ('image', models.ImageField(blank=True, help_text='登録しない場合は、デフォルトのイメージ写真を使用する', upload_to='user_', verbose_name='ツイートのイメージ写真')),
                ('liked', models.IntegerField(default=0, verbose_name='いいね数')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='投稿日時')),
                ('modified_at', models.DateTimeField(auto_now=True, verbose_name='更新日')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
