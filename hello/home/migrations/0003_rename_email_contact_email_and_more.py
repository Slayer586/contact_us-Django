# Generated by Django 4.2 on 2023-06-17 06:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_firstname_contact_firstname_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='Email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Firstname',
            new_name='firstname',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Lastname',
            new_name='lastname',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='Phone',
            new_name='phone',
        ),
    ]
