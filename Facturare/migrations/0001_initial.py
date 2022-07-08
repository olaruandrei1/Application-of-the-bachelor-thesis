# Generated by Django 4.0.4 on 2022-06-21 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Factura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pacient', models.CharField(max_length=100)),
                ('pacient_email', models.EmailField(blank=True, max_length=254, null=True)),
                ('adresa_facturare', models.TextField(blank=True, null=True)),
                ('data_emitere', models.DateField()),
                ('data_expirare', models.DateField(blank=True, null=True)),
                ('factura_d', models.TextField(default='this is a default message.')),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='LineItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serviciu', models.TextField()),
                ('descriere', models.TextField()),
                ('cantitate', models.IntegerField()),
                ('valoare_monetara', models.DecimalField(decimal_places=2, max_digits=9)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=9)),
                ('pacient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Facturare.factura')),
            ],
        ),
    ]