from django.db import models

class Location(models.Model):
    plz = models.CharField(max_length=5, verbose_name='Postleitzahl')
    gemeinde = models.CharField(max_length=255, verbose_name='Gemeinde')
    gemarkung = models.CharField(max_length=255, verbose_name='Gemarkung')
    flurstuecke = models.CharField(max_length=50, verbose_name='Flurstücke')
    breitengrad = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Breitengrad')
    laengengrad = models.DecimalField(max_digits=9, decimal_places=6, verbose_name='Ländengrad')
    groesse_der_bodenflaeche = models.DecimalField(max_digits=10, decimal_places=2,
                                                   verbose_name='Größe der Bodenfläche')
    ART_DER_BODENFLAECHE_CHOICES = [
        ('KONVERSIONSFLAECHE', 'Konversionsfläche'),
        ('GEBAEUDE', 'Gebäude'),
        ('AGRARFLAECHE', 'Agrarfläche'),
        ('SONSTIGE', 'Sonstige Freiflächen')
    ]
    art_der_bodenflaeche = models.CharField(max_length=100, choices=ART_DER_BODENFLAECHE_CHOICES,
                                            verbose_name='Art der Bodenfläche')


class Operations(models.Model):
    operation_type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # Assuming operations can be ongoing
    # Additional operations fields...

    def __str__(self):
        return self.operation_type

class SPV(models.Model):
    projektgesellschaft = models.CharField(max_length=255,verbose_name='Projektgesellschaft')
    onesolar_id = models.CharField(max_length=7, verbose_name='OneSolar ID')
    name = models.CharField(max_length=255, verbose_name='Name')
    spv_type = models.CharField(max_length=100, verbose_name='Typ der Projektgesellschaft')
    ZWECK_CHOICES = [
        ('SOLARPARK', 'Solarpark'),
        ('INFRASTRUKTURGESELLSCHAFT', 'Infrastrukturgesellschaft'),
        ('SONSTIGES', 'Sonstiges')
    ]
    zweck = models.CharField(max_length=100, choices=ZWECK_CHOICES,
                             verbose_name='Zweck der Projektgesellschaft')
    STAND_CHOICES = [
        ('EIGENBESTAND', 'Eigenbestand'),
        ('EXTERN', 'Extern'),
        ('IM BAU', 'Im Bau'),
        ('IM VERKAUFSPROZESS', 'Im Verkaufsprozess')
    ]
    stand = models.CharField(max_length=100, choices=STAND_CHOICES, verbose_name='Aktueller Stand')
    besonderheit = models.CharField(max_length=255, verbose_name='Besonderheit')

    location = models.OneToOneField(Location, on_delete=models.CASCADE, related_name='spv',
                                    verbose_name='Standortdaten')
    #operations = models.ManyToManyField(Operations, related_name='spvs')
    # Additional SPV fields...

    def __str__(self):
        return self.name
