# Generated by Django 5.1 on 2024-11-16 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='profile',
            new_name='profile_pic',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='Address',
        ),
        migrations.AddField(
            model_name='profile',
            name='address',
            field=models.ImageField(default=None, upload_to='andand'),
            preserve_default=False,
        ),
    ]