# Generated by Django 2.1.2 on 2018-10-23 00:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='cidade',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='endereco',
            name='estado',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='endereco',
            name='latitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='longitude',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='endereco',
            name='pais',
            field=models.CharField(default='1', max_length=70),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='endereco',
            name='linha2',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]