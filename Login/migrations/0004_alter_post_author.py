# Generated by Django 4.2.11 on 2024-04-14 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Login', '0003_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(max_length=100),
        ),
    ]