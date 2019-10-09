# Generated by Django 2.2.6 on 2019-10-02 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('docker', '0002_docker_related_names'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blob',
            name='digest',
            field=models.CharField(db_index=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='manifest',
            name='digest',
            field=models.CharField(db_index=True, max_length=255),
        ),
    ]