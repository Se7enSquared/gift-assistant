# Generated by Django 4.0.5 on 2022-06-12 18:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gift_app', '0013_alter_recipient_user_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipient',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
