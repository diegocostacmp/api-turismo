# Generated by Django 2.2.6 on 2019-10-24 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('atracao', '0002_atracao_foto'),
    ]

    operations = [
        migrations.AddField(
            model_name='atracao',
            name='observacao',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
