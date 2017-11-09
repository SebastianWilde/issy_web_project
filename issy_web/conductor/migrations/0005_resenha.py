# Generated by Django 2.0b1 on 2017-11-08 23:20

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conductor', '0004_auto_20171030_2347'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resenha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emisor', models.CharField(max_length=264)),
                ('estrellas', models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)])),
                ('comentario', models.TextField()),
                ('receptor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='conductor.Conductor')),
            ],
        ),
    ]