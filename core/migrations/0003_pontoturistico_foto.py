# Generated by Django 3.0.4 on 2020-03-24 16:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200324_1120'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='Foto',
            field=models.ImageField(blank=True, null=True, upload_to='pontosturisticos'),
        ),
    ]
