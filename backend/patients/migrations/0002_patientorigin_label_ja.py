# Generated by Django 3.0.3 on 2020-03-06 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientorigin',
            name='label_ja',
            field=models.CharField(default='', max_length=30),
            preserve_default=False,
        ),
    ]
