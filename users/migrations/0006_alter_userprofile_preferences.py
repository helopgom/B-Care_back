# Generated by Django 5.1 on 2024-09-06 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_userprofile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='preferences',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
