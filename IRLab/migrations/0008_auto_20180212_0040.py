# Generated by Django 2.0.2 on 2018-02-12 00:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IRLab', '0007_auto_20180212_0039'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='absolute_discount',
            options={},
        ),
        migrations.AlterModelOptions(
            name='dirichlet_prior',
            options={},
        ),
        migrations.AlterModelOptions(
            name='jelinek_mercer',
            options={},
        ),
        migrations.AlterModelOptions(
            name='okapi_bm25',
            options={},
        ),
        migrations.AlterModelOptions(
            name='pivoted_length',
            options={},
        ),
        migrations.AlterModelOptions(
            name='retrievalmethod',
            options={},
        ),
        migrations.RemoveField(
            model_name='retrievalmethod',
            name='polymorphic_ctype',
        ),
    ]
