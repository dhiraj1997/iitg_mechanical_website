# Generated by Django 2.2.1 on 2019-06-12 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0019_auto_20190611_1119'),
    ]

    operations = [
        migrations.AddField(
            model_name='alumnuspage',
            name='dupc',
            field=models.CharField(choices=[('6', 'Not Applicable'), ('0', 'Chairman'), ('1', 'Secretary'), ('2', 'Faculty Member'), ('3', 'External Member'), ('4', '3rd year BTech'), ('5', '2nd year BTech')], default='6', max_length=2),
        ),
        migrations.AddField(
            model_name='alumnuspage',
            name='mesa',
            field=models.CharField(choices=[('6', 'Not Applicable'), ('0', 'President'), ('1', 'Vice President'), ('2', 'Head'), ('3', 'Branch Representative'), ('4', 'Member'), ('5', 'Faculty Advisor')], default='5', max_length=2),
        ),
        migrations.AddField(
            model_name='alumnuspage',
            name='sae',
            field=models.CharField(choices=[('3', 'Not Applicable'), ('0', 'Chairman'), ('1', 'Other'), ('2', 'Faculty Advisor')], default='3', max_length=2),
        ),
        migrations.AddField(
            model_name='facultypage',
            name='mesa',
            field=models.CharField(choices=[('6', 'Not Applicable'), ('0', 'President'), ('1', 'Vice President'), ('2', 'Head'), ('3', 'Branch Representative'), ('4', 'Member'), ('5', 'Faculty Advisor')], default='5', max_length=2),
        ),
        migrations.AddField(
            model_name='facultypage',
            name='sae',
            field=models.CharField(choices=[('3', 'Not Applicable'), ('0', 'Chairman'), ('1', 'Other'), ('2', 'Faculty Advisor')], default='3', max_length=2),
        ),
        migrations.AddField(
            model_name='studentpage',
            name='dupc',
            field=models.CharField(choices=[('6', 'Not Applicable'), ('0', 'Chairman'), ('1', 'Secretary'), ('2', 'Faculty Member'), ('3', 'External Member'), ('4', '3rd year BTech'), ('5', '2nd year BTech')], default='6', max_length=2),
        ),
        migrations.AddField(
            model_name='studentpage',
            name='mesa',
            field=models.CharField(choices=[('6', 'Not Applicable'), ('0', 'President'), ('1', 'Vice President'), ('2', 'Head'), ('3', 'Branch Representative'), ('4', 'Member'), ('5', 'Faculty Advisor')], default='5', max_length=2),
        ),
        migrations.AddField(
            model_name='studentpage',
            name='sae',
            field=models.CharField(choices=[('3', 'Not Applicable'), ('0', 'Chairman'), ('1', 'Other'), ('2', 'Faculty Advisor')], default='3', max_length=2),
        ),
        migrations.AlterField(
            model_name='alumnuspage',
            name='specialization',
            field=models.CharField(choices=[('0', 'Not Applicable'), ('1', 'Aerodynamics & Propulsion'), ('2', 'Manufacturing Science and Engineering'), ('3', 'Computational Mechanics'), ('4', 'Fluids and Thermal'), ('5', 'Machine Design')], default='0', help_text='Not Applicable - for B.Tech, PhD and PostDocs', max_length=2),
        ),
        migrations.AlterField(
            model_name='studentpage',
            name='specialization',
            field=models.CharField(choices=[('0', 'Not Applicable'), ('1', 'Aerodynamics & Propulsion'), ('2', 'Manufacturing Science and Engineering'), ('3', 'Computational Mechanics'), ('4', 'Fluids and Thermal'), ('5', 'Machine Design')], default='0', help_text='Not Applicable - for B.Tech, PhD and PostDocs', max_length=2),
        ),
    ]
