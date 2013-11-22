from django.db import models

class LivelihoodZones(models.Model):
    description = models.CharField(max_length=200)

    class Meta:
    	verbose_name_plural = "Livelihood Zones"

    def __unicode__(self):
        return self.description


class Sectors(models.Model):
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Sectors"

    def __unicode__(self):
        return self.description
        

class Indicators(models.Model):
    indicator_id = models.IntegerField()
    description = models.CharField(max_length=200)
    sector = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = "Indicators"

    def __unicode__(self):
        return self.description


class Phases(models.Model):
    phase_id = models.IntegerField()
    description = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Phases"

    def __unicode__(self):
        return self.description
       

class Analysis(models.Model):
    district = models.IntegerField(default=0)
    year = models.PositiveSmallIntegerField(blank=True, null=True)
    month = models.PositiveSmallIntegerField(blank=True, null=True)
    livelihoodzones = models.ForeignKey(LivelihoodZones)
    sectors = models.ForeignKey(Sectors)
    indicators= models.ForeignKey(Indicators)
    value = models.FloatField(default=0)
    phase = models.IntegerField(default=0)
    adjustedphase = models.IntegerField(default=0)
    effectivephase = models.IntegerField(default=0)



      