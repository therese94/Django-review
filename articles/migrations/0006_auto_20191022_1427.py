# Generated by Django 2.2.4 on 2019-10-22 05:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0005_comment_uesr'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='uesr',
            new_name='user',
        ),
    ]