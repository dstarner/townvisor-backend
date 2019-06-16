# Generated by Django 2.2.2 on 2019-06-16 20:29

from django.db import migrations, models
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='published',
            field=models.BooleanField(default=False, help_text='Is the post published and public'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='Creation Time'),
        ),
        migrations.AlterField(
            model_name='post',
            name='last_modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='Last Modified Time'),
        ),
    ]
