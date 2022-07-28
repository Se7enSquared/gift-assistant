# Generated by Django 4.0.5 on 2022-07-24 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift_app', '0024_rename_created_on_gift_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipient',
            name='relationship',
            field=models.CharField(choices=[('Select', 'Select'), ('Spouse', 'Spouse'), ('Parent', 'Parent'), ('Aunt', 'Aunt'), ('Uncle', 'Uncle'), ('Child', 'Child'), ('Sibling', 'Sibling'), ('Friend', 'Friend'), ('Grandparent', 'Grandparent'), ('Cousin', 'Cousin'), ('Coworker', 'Coworker'), ('Other', 'Other')], default='Select', max_length=16),
        ),
    ]