from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class MicroChip(models.Model):
    IdMC = models.IntegerField(primary_key=True)
    SizeMC = models.IntegerField()
    NameMC = models.CharField(max_length=20)
    MaterMC = models.CharField(max_length=200)
    def __str__(self) -> str:
        return self.NameMC
    
class CompleteCulture(models.Model):
    IdCCulture = models.IntegerField(primary_key=True)
    IdMCCCulture = models.ForeignKey(MicroChip, on_delete=models.CASCADE, to_field='IdMC')
    DescriptionCCulture = models.CharField(max_length=500)
    StartDateCCulture = models.DateField()
    EndDateCCulture = models.DateField()
    PrepExpCCulture = models.CharField(max_length=200)

class Record(models.Model):
    IdRec = models.IntegerField(primary_key=True)
    PathRec = models.CharField(max_length=150)
    StartDateRec = models.DateField()
    
class Contain(models.Model):
    IdCCultureCont = models.ForeignKey(CompleteCulture, on_delete=models.CASCADE, to_field='IdCCulture')
    IdRecCont = models.ForeignKey(Record, on_delete=models.CASCADE, to_field='IdRec')
    RecStartDateCont = models.DateField()
    RecEndDateCont = models.DateField()
    CultureAgeStartCont = models.IntegerField()
    NameExpCont = models.CharField(max_length=100)
    
class SpikeFamily(models.Model):
    IdSF = models.IntegerField(primary_key=True)
    NameSF = models.CharField(max_length=20)
        
class Spike(models.Model):
    IdSpike = models.IntegerField(primary_key=True)
    MeasureSpike = models.IntegerField()
    AmplitudeSpike = models.IntegerField()
    DateSpike = models.DateField()
    NumElectrodeSpike = models.IntegerField()
    TresholdSpike = models.IntegerField()
    FormSpike = models.CharField(max_length=20)
    IdRecSpike = models.ForeignKey(Record, on_delete=models.CASCADE, to_field='IdRec')
    IdSFSpike = models.ForeignKey(SpikeFamily, on_delete=models.CASCADE, to_field='IdSF')
        

class ReceiverFamily(models.Model):
    
    INHIBITOR = 'IN'
    ACTIVATOR = 'AC'
    FAMILY_CHOICES = [
        (INHIBITOR, 'Inhibitor'),
        (ACTIVATOR, 'Activator')
    ]
    
    IdRF = models.IntegerField(primary_key=True)
    NameRF = models.CharField(max_length=20)
    TypeRD = models.CharField(max_length=2, choices=FAMILY_CHOICES)
    
class CompoundProduct(models.Model):
    IdCP = models.IntegerField(primary_key=True)
    NameCP = models.CharField(max_length=20)
    ConcentrationP = models.IntegerField()
        
class BelongRF(models.Model):
    IdCPBelong = models.ForeignKey(CompoundProduct, on_delete=models.CASCADE, to_field='IdCP')
    IdRF = models.ForeignKey(ReceiverFamily, on_delete=models.CASCADE, to_field='IdRF')
    
class Treat(models.Model):
    IdCCultureTreat = models.ForeignKey(CompleteCulture, on_delete=models.CASCADE, to_field='IdCCulture')
    IdCPTreat = models.ForeignKey(CompoundProduct, on_delete=models.CASCADE, to_field='IdCP')
    StartDateTreat = models.DateField()
    EndDateTreat = models.DateField()
    
    