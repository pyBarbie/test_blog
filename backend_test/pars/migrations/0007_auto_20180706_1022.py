# Generated by Django 2.0.6 on 2018-07-06 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pars', '0006_auto_20180706_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urlmodel',
            name='time',
            field=models.DateTimeField(null=True),
        ),
    ]
