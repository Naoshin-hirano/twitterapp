# Generated by Django 3.2.6 on 2021-09-29 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('twitterapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweetpost',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='tweetpost',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]