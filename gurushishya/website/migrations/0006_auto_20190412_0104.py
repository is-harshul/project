# Generated by Django 2.1.7 on 2019-04-11 19:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0005_auto_20190412_0102'),
    ]

    operations = [
        migrations.RenameField(
            model_name='signupuser',
            old_name='Password1',
            new_name='Password',
        ),
        migrations.RemoveField(
            model_name='signupuser',
            name='Password2',
        ),
    ]