# Generated by Django 3.0.2 on 2020-01-16 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_data_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='launchpad',
            name='missile',
            field=models.CharField(default=0, max_length=30),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='launchpad',
            name='altitude',
            field=models.FloatField(default=0, null=True),
        ),
    ]
