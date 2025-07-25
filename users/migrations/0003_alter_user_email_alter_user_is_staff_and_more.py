# Generated by Django 5.1.7 on 2025-04-25 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_user_student_id_alter_user_email_alter_user_password'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=200, unique=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='student_id',
            field=models.CharField(default='231400000', max_length=20),
        ),
    ]
