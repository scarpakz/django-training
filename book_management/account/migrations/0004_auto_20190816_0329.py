# Generated by Django 2.2.4 on 2019-08-16 03:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20190815_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='cover',
            field=models.FileField(blank=True, upload_to='images/'),
        ),
    ]