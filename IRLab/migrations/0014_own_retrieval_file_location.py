# Generated by Django 2.0.2 on 2018-02-23 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IRLab', '0013_code_own_retrieval'),
    ]

    operations = [
        migrations.AddField(
            model_name='own_retrieval',
            name='file_location',
            field=models.CharField(default='null', max_length=200),
            preserve_default=False,
        ),
    ]
