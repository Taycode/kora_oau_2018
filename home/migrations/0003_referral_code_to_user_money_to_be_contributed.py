# Generated by Django 2.0.3 on 2018-07-27 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20180727_1631'),
    ]

    operations = [
        migrations.AddField(
            model_name='referral_code_to_user',
            name='money_to_be_contributed',
            field=models.IntegerField(default=0),
        ),
    ]
