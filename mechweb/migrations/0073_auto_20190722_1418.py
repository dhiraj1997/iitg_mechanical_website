# Generated by Django 2.2.1 on 2019-07-22 14:18

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailimages', '0001_squashed_0021'),
        ('mechweb', '0072_auto_20190721_2226'),
    ]

    operations = [
        migrations.AddField(
            model_name='mechhomepage',
            name='donate_image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image'),
        ),
        migrations.AddField(
            model_name='mechhomepage',
            name='donate_message',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AddField(
            model_name='mechhomepage',
            name='donation_link',
            field=models.URLField(default='http://www.iitg.ac.in/mech/', max_length=250),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='aboutiitgmech',
            name='about',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='aboutiitgmech',
            name='history',
            field=models.CharField(blank=True, max_length=2000),
        ),
        migrations.AlterField(
            model_name='aboutiitgmech',
            name='vision',
            field=models.CharField(blank=True, max_length=2000),
        ),
    ]
