# Generated by Django 2.0.3 on 2018-07-28 15:48

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0006_auto_20180728_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='ajo_group_details',
            name='contributors_payed',
            field=models.ManyToManyField(related_name='_ajo_group_details_contributors_payed_+', to=settings.AUTH_USER_MODEL),
        ),
    ]