# Generated by Django 4.0.5 on 2022-06-04 05:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='recipient',
            options={'ordering': ['last_name']},
        ),
        migrations.RenameField(
            model_name='recipient',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='recipient',
            name='last_name',
            field=models.CharField(default='test', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipient',
            name='notes',
            field=models.TextField(),
        ),
    ]
