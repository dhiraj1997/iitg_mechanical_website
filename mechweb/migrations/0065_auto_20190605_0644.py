# Generated by Django 2.2.1 on 2019-06-05 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0064_hometextpanel_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hometextpanel',
            name='description',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]
