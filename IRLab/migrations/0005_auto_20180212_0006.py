# Generated by Django 2.0.2 on 2018-02-12 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IRLab', '0004_auto_20180211_2357'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='absolute_discount',
            name='ranker_id',
        ),
        migrations.RemoveField(
            model_name='dirichlet_prior',
            name='ranker_id',
        ),
        migrations.RemoveField(
            model_name='jelinek_mercer',
            name='ranker_id',
        ),
        migrations.RemoveField(
            model_name='okapi_bm25',
            name='ranker_id',
        ),
        migrations.RemoveField(
            model_name='pivoted_length',
            name='ranker_id',
        ),
        migrations.AddField(
            model_name='retrievalmethod',
            name='ranker_id',
            field=models.CharField(default='test', max_length=70),
            preserve_default=False,
        ),
    ]
