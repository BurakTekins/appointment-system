# Generated by Django 5.1.7 on 2025-04-13 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announcments', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcments',
            name='title',
            field=models.CharField(default='Genel Duyuru: ', max_length=200),
        ),
    ]
