# Generated by Django 4.0.5 on 2022-06-19 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gift_app', '0020_rename_unknown_birthyear_recipient_birth_year_unknown'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='occasion',
            options={'ordering': ['recipient']},
        ),
        migrations.RemoveField(
            model_name='occasion',
            name='name',
        ),
        migrations.AlterField(
            model_name='occasion',
            name='occasion_type',
            field=models.CharField(choices=[('BIRTHDAY', 'Birthday'), ('WEDDING_ANNIVERSARY', 'Wedding Anniversary'), ('DATING_ANNIVERSARY', 'Wedding Anniversary'), ('WORK_ANNIVERSARY', 'Work Anniversary'), ('FRIENDIVERSARY', 'Friendship Anniversary'), ('GRADUATION', 'Graduation'), ('BABY_SHOWER', 'Baby Shower'), ('WEDDING', 'Wedding'), ('THANKS', 'Thanks'), ('JUST_BECAUSE', 'Just Because')], default='JUST_BECAUSE', max_length=50),
        ),
        migrations.AlterField(
            model_name='recipient',
            name='birth_month',
            field=models.IntegerField(choices=[(0, 'Select'), (1, 'January'), (2, 'February'), (3, 'March'), (4, 'April'), (5, 'May'), (6, 'June'), (7, 'July'), (8, 'August'), (9, 'September'), (10, 'October'), (11, 'November'), (12, 'December')], default=0),
        ),
    ]
