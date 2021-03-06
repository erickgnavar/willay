# Generated by Django 2.0.5 on 2018-06-11 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('claims', '0002_claim_verified'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='marker_icon',
            field=models.ImageField(blank=True, help_text='32x32 png image is required', null=True, upload_to='claims/category/marker_icon/%Y/%m/%d/', verbose_name='Marker icon'),
        ),
    ]
