# Generated by Django 4.0.4 on 2022-06-18 13:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Gestiune', '0005_rename_pacient_id_fise_prezentare_pacient'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fise_internari',
            old_name='Pacient',
            new_name='pacient',
        ),
    ]