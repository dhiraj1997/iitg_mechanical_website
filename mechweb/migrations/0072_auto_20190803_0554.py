# Generated by Django 2.2.1 on 2019-08-03 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('mechweb', '0071_facultypreviouswork'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechhomepage',
            name='HOD_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='mechhomepage',
            name='donate_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailimages.Image'),
        ),
    ]
