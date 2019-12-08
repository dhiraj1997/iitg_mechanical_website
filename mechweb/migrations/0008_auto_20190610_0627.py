# Generated by Django 2.2.1 on 2019-06-10 06:27

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.core.fields


class Migration(migrations.Migration):

    dependencies = [
        ('mechweb', '0007_auto_20190609_1319'),
    ]

    operations = [
        migrations.AddField(
            model_name='coursestructure',
            name='intro',
            field=wagtail.core.fields.RichTextField(blank=True),
        ),
        migrations.AlterField(
            model_name='coursepage',
            name='credits',
            field=models.IntegerField(verbose_name='C'),
        ),
        migrations.AlterField(
            model_name='coursepage',
            name='lectures',
            field=models.IntegerField(verbose_name='L'),
        ),
        migrations.AlterField(
            model_name='coursepage',
            name='practicals',
            field=models.IntegerField(verbose_name='P'),
        ),
        migrations.AlterField(
            model_name='coursepage',
            name='tutorials',
            field=models.IntegerField(verbose_name='T'),
        ),
        migrations.AlterField(
            model_name='coursepagefaculty',
            name='session',
            field=models.DateField(verbose_name='Instruction start date'),
        ),
        migrations.CreateModel(
            name='FeaturedResearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('featured_research', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='featured_research', to='mechweb.PublicationPage')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_research', to='mechweb.ResearchHomePage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FeaturedCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('featured_course', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='featured_course', to='mechweb.CoursePage')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='featured_course', to='mechweb.CourseStructure')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]