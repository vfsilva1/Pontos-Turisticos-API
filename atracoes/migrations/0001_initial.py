# Generated by Django 3.0.4 on 2020-03-23 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Atracao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=150)),
                ('Descricao', models.TextField()),
                ('HorarioFuncionamento', models.TextField()),
                ('IdadeMinima', models.IntegerField()),
            ],
        ),
    ]
