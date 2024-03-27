# Generated by Django 4.1 on 2024-03-27 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spv_master_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='art_der_bodenflaeche',
            field=models.CharField(choices=[('KONVERSIONSFLAECHE', 'Konversionsfläche'), ('GEBAEUDE', 'Gebäude'), ('AGRARFLAECHE', 'Agrarfläche'), ('SONSTIGE', 'Sonstige Freiflächen')], max_length=100, verbose_name='Art der Bodenfläche'),
        ),
        migrations.AlterField(
            model_name='location',
            name='breitengrad',
            field=models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Breitengrad'),
        ),
        migrations.AlterField(
            model_name='location',
            name='flurstuecke',
            field=models.CharField(max_length=50, verbose_name='Flurstücke'),
        ),
        migrations.AlterField(
            model_name='location',
            name='gemarkung',
            field=models.CharField(max_length=255, verbose_name='Gemarkung'),
        ),
        migrations.AlterField(
            model_name='location',
            name='gemeinde',
            field=models.CharField(max_length=255, verbose_name='Gemeinde'),
        ),
        migrations.AlterField(
            model_name='location',
            name='groesse_der_bodenflaeche',
            field=models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Größe der Bodenfläche'),
        ),
        migrations.AlterField(
            model_name='location',
            name='laengengrad',
            field=models.DecimalField(decimal_places=6, max_digits=9, verbose_name='Ländengrad'),
        ),
        migrations.AlterField(
            model_name='location',
            name='plz',
            field=models.CharField(max_length=5, verbose_name='Postleitzahl'),
        ),
    ]