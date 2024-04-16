from django.db import models
from spv_master_data.validators import validate_iban

# Location model
class Location(models.Model):
    plz = models.CharField(max_length=5, verbose_name='Postleitzahl')
    gemeinde = models.CharField(max_length=100, verbose_name='Gemeinde')
    gemarkung = models.CharField(max_length=100, verbose_name='Gemarkung')
    flurstuecke = models.CharField(max_length=50, verbose_name='Flurstücke')
    breitengrad = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Breitengrad')
    laengengrad = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Längengrad')
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


# Data of company model (Unternehmensdaten)
class Company(models.Model):
    handelsnummer = models.CharField(max_length=15, verbose_name='Handelsnummer')
    gericht = models.CharField(max_length=100, verbose_name='Gericht')
    steuernummer = models.CharField(max_length=13, verbose_name='Steuernummer')
    ust_id = models.CharField(max_length=11, verbose_name='Umsatzsteuer-ID')
    iban_hausbank = models.CharField(max_length=34, verbose_name='IBAN Hausbank',
                                     validators=[validate_iban])
    bic_hausbank = models.CharField(max_length=11, verbose_name='BIC Hausbank')
    hausbank = models.CharField(max_length=100, verbose_name='Hausbank')
    iban_kreditgeber = models.CharField(max_length=34, verbose_name='IBAN Finanzierende Bank',
                                        validators=[validate_iban])
    bic_kreditgeber = models.CharField(max_length=11, verbose_name='BIC Finanzierende Bank')
    kreditgeber = models.CharField(max_length=100, verbose_name='Finanzierende Bank')
    komplementaer_1 = models.CharField(max_length=15, verbose_name='Komplementär I')
    komplementaer_2 = models.CharField(max_length=15, verbose_name='Komplementär II', blank=True)
    kommanditist_1 = models.CharField(max_length=15, verbose_name='Kommanditist I')
    kommanditist_2 = models.CharField(max_length=15, verbose_name='Kommanditist II', blank=True)
    kommanditist_3 = models.CharField(max_length=15, verbose_name='Kommanditist III', blank=True)
    kommanditist_4 = models.CharField(max_length=15, verbose_name='Kommanditist IV', blank=True)
    kommanditist_5 = models.CharField(max_length=15, verbose_name='Kommanditist V', blank=True)


# Data of important milestones
class Milestones(models.Model):
    satzungsbeschluss = models.DateField(verbose_name='Satzungsbeschluss', blank=True)
    baustart = models.DateField(verbose_name='Baustart', blank=True)
    inbetriebnahme = models.DateField(verbose_name='Inbetriebnahme', blank=True)
    eeg_inbetriebnahme = models.DateField(verbose_name='EEG-Inbetriebnahme', blank=True)
    zuschlag_eeg = models.DateField(verbose_name='Zuschlag aus EEG-Ausschreibung', blank=True)
    ppa_abschluss = models.DateField(verbose_name='Abschluss PPA', blank=True)
    finanzierung_abschluss = models.DateField(verbose_name='Abschluss Finanzierung', blank=True)


# Main SPV model with the main data fields (Hauptdaten)
class SPV(models.Model):
    projektgesellschaft = models.CharField(max_length=255, verbose_name='Projektgesellschaft')
    onesolar_id = models.CharField(max_length=7, verbose_name='OneSolar ID')
    name = models.CharField(max_length=255, verbose_name='Vollständiger Name')
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
    besonderheit = models.CharField(max_length=255, verbose_name='Besonderheit', blank=True)

    # Add location model
    location = models.OneToOneField(Location, on_delete=models.CASCADE, related_name='spv',
                                    verbose_name='Standortdaten')

    # Add company model
    company = models.OneToOneField(Company, on_delete=models.CASCADE, related_name='spv',
                                   verbose_name='Unternehmensdaten', null=True)

    # Add milestones model
    milestones = models.OneToOneField(Milestones, on_delete=models.CASCADE, related_name='spv',
                                   verbose_name='Meilensteine', null=True)
    def __str__(self):
        return self.name





