# Generated by Django 3.1.3 on 2020-11-07 12:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_delete_readmember'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReadMember',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('boardModel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.boardmodel')),
            ],
        ),
    ]
