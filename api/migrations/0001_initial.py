# Generated by Django 3.1.1 on 2020-10-05 11:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=100, verbose_name='Descrição')),
                ('preco', models.FloatField(verbose_name='Preço')),
                ('qtde_disponivel', models.IntegerField(verbose_name='Quantidade disponível')),
                ('ativo', models.BooleanField(default=True)),
                ('data_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Data de inclusão')),
                ('data_alteracao', models.DateTimeField(null=True, verbose_name='Data de alteração')),
                ('data_exclusao', models.DateTimeField(null=True, verbose_name='Data de exclusão')),
                ('user_inclusao', models.CharField(max_length=50, verbose_name='Usuário inclusão')),
                ('user_alteracao', models.CharField(max_length=50, null=True, verbose_name='Usuário alteração')),
                ('user_exclusao', models.CharField(max_length=50, null=True, verbose_name='Usuário exclusão')),
            ],
            options={
                'verbose_name_plural': 'Produtos',
            },
        ),
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.CharField(max_length=100, null=True, verbose_name='Descrição')),
                ('ativo', models.BooleanField(default=True)),
                ('data_inclusao', models.DateTimeField(auto_now_add=True, verbose_name='Data de inclusão')),
                ('produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.produto')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
    ]
