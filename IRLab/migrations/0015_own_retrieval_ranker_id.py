# Generated by Django 2.0.2 on 2018-02-23 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IRLab', '0014_own_retrieval_file_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='own_retrieval',
            name='ranker_id',
            field=models.CharField(default='CustomizedRanker', max_length=70),
        ),
    ]
