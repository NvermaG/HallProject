# Generated by Django 3.2.4 on 2021-06-20 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0003_auto_20210620_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='hallbooking',
            name='day',
            field=models.DateField(null=True),
        ),
    ]