# Generated by Django 4.1 on 2022-09-04 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0003_tag_wantedperson'),
    ]

    operations = [
        migrations.AlterField(
            model_name='missingperson',
            name='missing_date',
            field=models.CharField(max_length=200),
        ),
    ]
