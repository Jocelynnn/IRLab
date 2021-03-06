# Generated by Django 2.0.2 on 2018-02-11 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IRLab', '0003_auto_20180206_1845'),
    ]

    operations = [
        migrations.AddField(
            model_name='absolute_discount',
            name='ranker_id',
            field=models.CharField(default='AbsoluteDiscount', max_length=70),
        ),
        migrations.AddField(
            model_name='dirichlet_prior',
            name='ranker_id',
            field=models.CharField(default='DirichletPrior', max_length=70),
        ),
        migrations.AddField(
            model_name='jelinek_mercer',
            name='ranker_id',
            field=models.CharField(default='JelinekMercer', max_length=70),
        ),
        migrations.AddField(
            model_name='okapi_bm25',
            name='ranker_id',
            field=models.CharField(default='OkapiBM25', max_length=70),
        ),
        migrations.AddField(
            model_name='pivoted_length',
            name='ranker_id',
            field=models.CharField(default='PivotedLength', max_length=70),
        ),
    ]
