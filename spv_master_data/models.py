from django.db import models

class Location(models.Model):
    plz = models.CharField(max_length=5)
    gemeinde = models.CharField(max_length=255)
    gemarkung = models.CharField(max_length=255)
    flurstuecke = models.CharField(max_length=50)
    breitengrad = models.DecimalField(max_digits=9, decimal_places=6)
    laengengrad = models.DecimalField(max_digits=9, decimal_places=6)
    groesse_der_bodenflaeche = models.DecimalField(max_digits=10, decimal_places=2)
    ART_DER_BODENFLAECHE_CHOICES = [
        ('KONVERSIONSFLAECHE', 'Konversionsfläche'),
        ('GEBAEUDE', 'Gebäude'),
        ('AGRARFLAECHE', 'Agrarfläche'),
        ('SONSTIGE', 'Sonstige Freiflächen')
    ]
    art_der_bodenflaeche = models.CharField(max_length=100, choices=ART_DER_BODENFLAECHE_CHOICES)


class Operations(models.Model):
    operation_type = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)  # Assuming operations can be ongoing
    # Additional operations fields...

    def __str__(self):
        return self.operation_type

class SPV(models.Model):
    projektgesellschaft = models.CharField(max_length=255)
    onesolar_id = models.CharField(max_length=7)
    name = models.CharField(max_length=255)
    spv_type = models.CharField(max_length=100)
    ZWECK_CHOICES = [
        ('SOLARPARK', 'Solarpark'),
        ('INFRASTRUKTURGESELLSCHAFT', 'Infrastrukturgesellschaft'),
        ('SONSTIGES', 'Sonstiges')
    ]
    zweck = models.CharField(max_length=100, choices=ZWECK_CHOICES)
    STAND_CHOICES = [
        ('EIGENBESTAND', 'Eigenbestand'),
        ('EXTERN', 'Extern'),
        ('IM BAU', 'Im Bau'),
        ('IM VERKAUFSPROZESS', 'Im Verkaufsprozess')
    ]
    stand = models.CharField(max_length=100, choices=STAND_CHOICES)
    besonderheit = models.CharField(max_length=255)

    location = models.OneToOneField(Location, on_delete=models.CASCADE, related_name='spv')
    operations = models.ManyToManyField(Operations, related_name='spvs')
    # Additional SPV fields...

    def __str__(self):
        return self.name
