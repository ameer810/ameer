# Generated by Django 3.0.7 on 2020-06-30 17:51

from django.db import migrations, models
import job.models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0002_job_owner'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=job.models.image_upload),
        ),
    ]
