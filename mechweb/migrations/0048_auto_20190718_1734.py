# Generated by Django 2.2.1 on 2019-07-18 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0047_auto_20190718_1414'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventpage',
            name='venue',
            field=models.CharField(blank=True, choices=[('0', 'Seminar hall'), ('1', 'ME new meeting room'), ('2', 'Other')], default='0', max_length=50),
        ),
    ]