# Generated by Django 4.1.3 on 2022-12-07 23:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('noticia', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='mombre',
            new_name='nombre',
        ),
    ]
