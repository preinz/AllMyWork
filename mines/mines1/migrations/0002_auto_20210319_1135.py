# Generated by Django 3.1.7 on 2021-03-19 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mines1', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='numbersOfPoints',
            new_name='Contact',
        ),
        migrations.RenameField(
            model_name='profile',
            old_name='name',
            new_name='Email',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='imageUrl',
        ),
        migrations.AddField(
            model_name='profile',
            name='Message',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
