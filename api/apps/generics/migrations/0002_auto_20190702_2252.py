# Generated by Django 2.2.2 on 2019-07-02 22:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
        ('generics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='like',
            name='creator',
            field=models.ForeignKey(help_text='Who is doing the liking', on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='flag',
            name='content_type',
            field=models.ForeignKey(limit_choices_to=models.Q(('app_label', 'posts'), ('app_label', 'users'), _connector='OR'), on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='flag',
            name='creator',
            field=models.ForeignKey(help_text='Who performed the flag', on_delete=django.db.models.deletion.CASCADE, related_name='flags', to=settings.AUTH_USER_MODEL),
        ),
    ]
