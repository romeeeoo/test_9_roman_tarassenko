# Generated by Django 4.1.3 on 2022-11-26 07:44

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='picture',
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
