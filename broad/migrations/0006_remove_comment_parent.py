# Generated by Django 3.0.7 on 2020-09-08 09:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('broad', '0005_auto_20200908_0854'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='parent',
        ),
    ]
