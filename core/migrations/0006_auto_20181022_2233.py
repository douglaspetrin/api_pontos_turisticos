# Generated by Django 2.1.2 on 2018-10-23 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_pontoturistico_endereco'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pontoturistico',
            name='endereco',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='enderecos.Endereco'),
        ),
    ]