# Generated by Django 2.2.2 on 2019-06-16 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_auto_20190616_2006'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='about',
            field=models.TextField(default="I haven't filled my About section out yet!"),
        ),
    ]
