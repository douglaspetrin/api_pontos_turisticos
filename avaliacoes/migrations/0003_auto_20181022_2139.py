# Generated by Django 2.1.2 on 2018-10-23 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avaliacoes', '0002_auto_20181022_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='avaliacao',
            name='nota',
            field=models.DecimalField(decimal_places=3, max_digits=4),
        ),
    ]