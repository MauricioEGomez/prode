# Generated by Django 5.1.7 on 2025-04-11 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_alter_fechaprode_cierre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partido',
            name='estadio',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
