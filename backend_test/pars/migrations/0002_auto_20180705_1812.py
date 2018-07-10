# Generated by Django 2.0.6 on 2018-07-05 18:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pars', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='H1_tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.TextField(blank=True, max_length=10000, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='urlmodel',
            name='charset',
            field=models.CharField(blank=True, help_text='encode from url', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='urlmodel',
            name='title',
            field=models.CharField(blank=True, default=None, help_text='title from url', max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='urlmodel',
            name='url',
            field=models.URLField(default=None, help_text='Input url for parse'),
        ),
        migrations.AddField(
            model_name='h1_tag',
            name='url',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='h1_tags', to='pars.UrlModel'),
        ),
    ]
