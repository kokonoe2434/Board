# Generated by Django 3.1.3 on 2020-11-09 09:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201109_1418'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='address1',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='address2',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='zipnumber',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
