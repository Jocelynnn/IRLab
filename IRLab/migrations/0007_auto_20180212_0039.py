# Generated by Django 2.0.2 on 2018-02-12 00:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        ('IRLab', '0006_auto_20180212_0024'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='absolute_discount',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='dirichlet_prior',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='jelinek_mercer',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='okapi_bm25',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='pivoted_length',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AlterModelOptions(
            name='retrievalmethod',
            options={'base_manager_name': 'objects'},
        ),
        migrations.AddField(
            model_name='retrievalmethod',
            name='polymorphic_ctype',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_irlab.retrievalmethod_set+', to='contenttypes.ContentType'),
        ),
    ]