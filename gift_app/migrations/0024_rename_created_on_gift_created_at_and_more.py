# Generated by Django 4.0.5 on 2022-07-20 03:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gift_app', '0023_alter_occasion_options_remove_recipient_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gift',
            old_name='created_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='gift',
            old_name='updated_on',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='occasion',
            old_name='created_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='occasion',
            old_name='updated_on',
            new_name='updated_at',
        ),
        migrations.RenameField(
            model_name='recipient',
            old_name='created_on',
            new_name='created_at',
        ),
        migrations.RenameField(
            model_name='recipient',
            old_name='updated_on',
            new_name='updated_at',
        ),
    ]
