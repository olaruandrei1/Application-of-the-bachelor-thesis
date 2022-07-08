# Generated by Django 4.0.4 on 2022-06-15 19:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Pacient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeprenumepacient', models.CharField(max_length=60)),
                ('CNP_Pacient', models.IntegerField()),
                ('telefon_Pacient', models.IntegerField()),
                ('emailPacient', models.CharField(max_length=60)),
                ('optiune_gen', models.CharField(choices=[('M', 'M'), ('F', 'F'), ('A', 'Altul')], max_length=1)),
                ('adresa_Pacient', models.CharField(max_length=100)),
                ('tip_cetatenie', models.CharField(choices=[('RO', 'Română'), ('CE', 'Cetățean european'), ('PS', 'Permis de ședere'), ('NS', 'nespecificat')], max_length=20)),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now)),
                ('autor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Fise_Prezentare',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('simptome_initiale', models.CharField(max_length=100)),
                ('optiune_specialitate', models.CharField(choices=[('NE', 'Neurologie'), ('GS', 'Gastroenterologie'), ('BI', 'Medicină Internă/Boli Interne'), ('ND', 'Nutriție și Diabet'), ('CD', 'Cardiologie'), ('DM', 'Dermatologie(Venerologie)'), ('OC', 'Oncologie'), ('UR', 'Urologie'), ('PD', 'Pediatrie'), ('OF', 'Oftalmologie'), ('OG', 'Obstetrică Ginecologie')], max_length=60)),
                ('concluzie_Consult', models.CharField(max_length=100, null=True)),
                ('optiune_Decizie', models.CharField(choices=[('CA', 'Consult & Ambulator'), ('CI', 'Consult & Internare de Zi'), ('IN', 'Internare'), ('TR', 'Tratament'), ('CZ', 'Cerere analize')], max_length=50)),
                ('optiune_plata', models.CharField(choices=[('AC', 'Asigurare CNAS'), ('DD', 'Decontare directă'), ('PT', 'Parteneriat*'), ('PF', 'Persoană fizică'), ('SP', 'Scutit plată')], max_length=40)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Pacient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestiune.pacient')),
            ],
        ),
        migrations.CreateModel(
            name='Fise_Internari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('Data_externare_internare', models.DateTimeField()),
                ('sectie_internare', models.CharField(choices=[('NE', 'Neurologie'), ('GS', 'Gastroenterologie'), ('BI', 'Medicină Internă/Boli Interne'), ('ND', 'Nutriție și Diabet'), ('CD', 'Cardiologie'), ('DM', 'Dermatologie(Venerologie)'), ('OC', 'Oncologie'), ('UR', 'Urologie'), ('PD', 'Pediatrie'), ('OF', 'Oftalmologie'), ('OG', 'Obstetrică Ginecologie')], max_length=50)),
                ('diagnostic_int_initial', models.CharField(max_length=100)),
                ('Epicriza_internare', models.CharField(max_length=100, null=True)),
                ('Pacient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Gestiune.pacient')),
            ],
        ),
    ]