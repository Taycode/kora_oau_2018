# Generated by Django 2.0.3 on 2018-07-28 11:31

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0004_auto_20180728_1231'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ajo_Group_Details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ajo_code', models.IntegerField(unique=True)),
                ('money_to_be_contributed', models.IntegerField(default=0)),
                ('contributors', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]