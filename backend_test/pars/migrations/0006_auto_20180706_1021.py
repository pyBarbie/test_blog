# Generated by Django 2.0.6 on 2018-07-06 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pars', '0005_auto_20180706_1020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlmodel',
            name='time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]