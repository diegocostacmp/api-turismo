# Generated by Django 2.2.6 on 2019-10-24 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_auto_20191024_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='docidentificacao',
            name='descricao',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
