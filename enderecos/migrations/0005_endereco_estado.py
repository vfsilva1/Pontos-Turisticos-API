# Generated by Django 3.0.4 on 2020-03-23 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enderecos', '0004_auto_20200323_1229'),
    ]

    operations = [
        migrations.AddField(
            model_name='endereco',
            name='Estado',
            field=models.CharField(default='SP', max_length=50),
        ),
    ]
