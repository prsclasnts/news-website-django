# Generated by Django 5.0.3 on 2024-03-21 04:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_news'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Categoria', 'verbose_name_plural': 'Categorias'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'Notícias'},
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=256)),
                ('comment', models.TextField()),
                ('status', models.BooleanField(default=False)),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.news')),
            ],
        ),
    ]