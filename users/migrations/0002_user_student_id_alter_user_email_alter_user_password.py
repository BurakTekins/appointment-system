# Generated by Django 5.1.7 on 2025-04-13 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='student_id',
            field=models.CharField(default='231400000', max_length=200),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=500),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=200),
        ),
    ]
