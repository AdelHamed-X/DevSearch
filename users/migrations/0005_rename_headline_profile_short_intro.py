# Generated by Django 5.0.6 on 2024-05-26 14:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_skill'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='headline',
            new_name='short_intro',
        ),
    ]
