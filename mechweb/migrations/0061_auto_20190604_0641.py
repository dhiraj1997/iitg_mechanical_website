# Generated by Django 2.2.1 on 2019-06-04 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0060_merge_20190603_1301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumnuspage',
            name='programme',
            field=models.CharField(choices=[('0', 'Bachelor'), ('1', 'Masters'), ('2', 'Research Scholar'), ('3', 'PostDoc')], default='0', max_length=2),
        ),
        migrations.AlterField(
            model_name='coursepage',
            name='eligible_programmes',
            field=models.CharField(choices=[('0', 'Bachelor'), ('1', 'Masters'), ('2', 'Research Scholar'), ('3', 'PostDoc')], default='0', max_length=100, verbose_name='Minimum qualification'),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='event_type',
            field=models.CharField(choices=[('0', 'Meeting'), ('1', 'Seminar'), ('2', 'Workshop'), ('3', 'Informal event'), ('4', 'Conference'), ('5', 'PhD viva')], default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='eventpage',
            name='venue',
            field=models.CharField(blank=True, choices=[('0', 'Seminar hall')], default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='facultypage',
            name='additional_roles',
            field=models.CharField(choices=[('2', 'Not Applicable'), ('1', 'HoD'), ('0', 'Director')], default='2', max_length=2),
        ),
        migrations.AlterField(
            model_name='facultypage',
            name='designation',
            field=models.CharField(choices=[('0', 'HAG'), ('1', 'Professor'), ('2', 'Assistant Professor'), ('3', 'Associate Professor'), ('4', 'Visiting Professor'), ('5', 'Professor On lien')], default='3', max_length=2),
        ),
        migrations.AlterField(
            model_name='facultypage',
            name='disciplinary_committee',
            field=models.CharField(choices=[('4', 'Not Applicable'), ('0', 'Chairman'), ('1', 'Secretary'), ('2', 'Member Secretary'), ('3', 'Student Member')], default='4', max_length=2),
        ),
        migrations.AlterField(
            model_name='facultypage',
            name='disposal_committee',
            field=models.CharField(choices=[('4', 'Not Applicable'), ('0', 'Chairman'), ('1', 'Member'), ('2', 'External Member'), ('3', 'Non Member Secretary')], default='4', max_length=2),
        ),
        migrations.AlterField(
            model_name='facultypage',
            name='dppc',
            field=models.CharField(choices=[('6', 'Not Applicable'), ('0', 'Chairman'), ('1', 'Secretary'), ('2', 'Faculty Member'), ('3', 'External Member'), ('4', 'PhD Student Member'), ('5', 'MTech Student Member')], default='6', max_length=2),
        ),
        migrations.AlterField(
            model_name='facultypage',
            name='dupc',
            field=models.CharField(choices=[('6', 'Not Applicable'), ('0', 'Chairman'), ('1', 'Secretary'), ('2', 'Faculty Member'), ('3', 'External Member'), ('4', '3rd year BTech'), ('5', '2nd year BTech')], default='6', max_length=2),
        ),
        migrations.AlterField(
            model_name='facultypage',
            name='faculty_in_charge',
            field=models.CharField(choices=[('11', 'Not Applicable'), ('0', 'BTP Co ordinator'), ('1', 'MTP Co ordinator'), ('2', 'Central Workshop'), ('3', 'Library Committee'), ('4', 'Training and Placement'), ('5', 'Departmental Seminar Room'), ('6', 'Secretary Faculty Meeting'), ('7', 'PG Computational Lab'), ('8', 'Research Scholar Room'), ('9', 'Time Table Committee'), ('10', 'Departmental Website')], default='11', max_length=2),
        ),
        migrations.AlterField(
            model_name='facultypage',
            name='laboratory_in_charge',
            field=models.CharField(choices=[('14', 'Not Applicable'), ('0', 'Advanced Manufacturing Laboratory'), ('1', 'CAD Laboratory'), ('2', 'Central Workshop'), ('3', 'Fluid Mechanics Laboratory'), ('4', 'IC Engines Laboratory'), ('5', 'Instrumentation and Control Laboratory'), ('6', 'Material Science Laboratory'), ('7', 'Tribology Laboratory'), ('8', 'Mechatronics and Robotics Laboratory'), ('9', 'Strength of Materials Laboratory'), ('10', 'Theory of Machines Laboratory'), ('11', 'Thermal Science Laboratory'), ('12', 'Turbo Machinary Laboratory'), ('13', 'Vibrations and Acoustics Laboratory')], default='14', max_length=2),
        ),
        migrations.AlterField(
            model_name='hometextpanel',
            name='content_type',
            field=models.CharField(choices=[('0', 'Mini article')], default='0', max_length=50),
        ),
        migrations.AlterField(
            model_name='projectpage',
            name='project_type',
            field=models.CharField(choices=[('1', 'Academic'), ('0', 'Consultancy')], default='1', max_length=20),
        ),
        migrations.AlterField(
            model_name='staffpage',
            name='designation',
            field=models.CharField(choices=[('0', 'Administrative Staff'), ('1', 'Project Staff'), ('2', 'Lab Staff'), ('3', 'Technicial staff'), ('4', 'Others')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='studentpage',
            name='programme',
            field=models.CharField(choices=[('0', 'Bachelor'), ('1', 'Masters'), ('2', 'Research Scholar'), ('3', 'PostDoc')], default='0', max_length=2),
        ),
    ]
