# Generated by Django 2.2.7 on 2019-11-19 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='QuemSomos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Sobre nós')),
                ('image', models.ImageField(upload_to='aboutUs/', verbose_name='Imagem')),
            ],
            options={
                'verbose_name': 'Quem somos',
            },
        ),
    ]
