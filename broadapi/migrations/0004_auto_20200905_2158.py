# Generated by Django 3.0.7 on 2020-09-05 21:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('broadapi', '0003_auto_20200905_1829'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='broad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='broadapi.Broad'),
        ),
    ]
