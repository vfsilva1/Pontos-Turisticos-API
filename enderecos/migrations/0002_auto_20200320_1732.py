# Generated by Django 3.0.4 on 2020-03-20 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='endereco',
            name='Latitude',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='Linha2',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='endereco',
            name='Longitude',
            field=models.IntegerField(null=True),
        ),
    ]
