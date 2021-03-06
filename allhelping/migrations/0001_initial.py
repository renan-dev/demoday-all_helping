# Generated by Django 2.2.4 on 2019-08-14 13:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ajudado',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=255, verbose_name='Sobrenome')),
                ('email', models.EmailField(max_length=255, verbose_name='E-mail')),
                ('telefone', models.CharField(max_length=255, verbose_name='Telefone')),
                ('ativo', models.BooleanField(default=True)),
                ('data_de_criacao', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ajudante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=255, verbose_name='Nome')),
                ('sobrenome', models.CharField(max_length=255, verbose_name='Sobrenome')),
                ('email', models.EmailField(max_length=255, verbose_name='E-mail')),
                ('telefone', models.CharField(max_length=255, verbose_name='Telefone')),
                ('ativo', models.BooleanField(default=True)),
                ('data_de_criacao', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ID_ajudado', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allhelping.Ajudado')),
                ('ID_ajudante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allhelping.Ajudante')),
            ],
        ),
        migrations.CreateModel(
            name='Mensagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensagem', models.CharField(max_length=255, verbose_name='Mensagem')),
                ('remetente', models.EmailField(max_length=255, verbose_name='Remetente')),
                ('telefone', models.CharField(max_length=255, verbose_name='Telefone')),
                ('data', models.DateField(auto_now_add=True)),
                ('ID_match', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='allhelping.Match')),
            ],
        ),
    ]
