# Generated by Django 2.0.2 on 2018-04-17 23:28

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('IRLab', '0016_auto_20180224_2024'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Own_retrieval',
            new_name='Customized_retrieval',
        ),
        migrations.DeleteModel(
            name='Code',
        ),
        migrations.RemoveField(
            model_name='post',
            name='author',
        ),
        migrations.DeleteModel(
            name='Post',
        ),
    ]
