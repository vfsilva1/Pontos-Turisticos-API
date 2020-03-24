# Generated by Django 3.0.4 on 2020-03-23 14:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('comentarios', '0001_initial'),
        ('avaliacoes', '0001_initial'),
        ('atracoes', '0001_initial'),
        ('enderecos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PontoTuristico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nome', models.CharField(max_length=150)),
                ('Descricao', models.TextField()),
                ('Aprovado', models.BooleanField(default=False)),
                ('Atracoes', models.ManyToManyField(to='atracoes.Atracao')),
                ('Avaliacoes', models.ManyToManyField(to='avaliacoes.Avaliacao')),
                ('Comentarios', models.ManyToManyField(to='comentarios.Comentario')),
                ('Endereco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='enderecos.Endereco')),
            ],
        ),
    ]
