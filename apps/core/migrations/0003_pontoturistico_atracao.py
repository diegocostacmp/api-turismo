# Generated by Django 2.2.6 on 2019-10-21 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracao', '0001_initial'),
        ('core', '0002_auto_20191021_1259'),
    ]

    operations = [
        migrations.AddField(
            model_name='pontoturistico',
            name='atracao',
            field=models.ManyToManyField(to='atracao.Atracao'),
        ),
    ]