# Generated by Django 4.0.5 on 2022-06-12 21:12

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gift_app', '0014_alter_recipient_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='gift',
            name='date_given',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
