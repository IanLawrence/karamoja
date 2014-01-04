from django.db import models

class Districts(models.Model):
    district_id = models.IntegerField(unique=True)
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=200)


    class Meta:
        verbose_name_plural = "Districts"

    def __unicode__(self):
        return self.name

class Years(models.Model):
    yearly = models.IntegerField()

    class Meta:
        verbose_name_plural = "Years"

    def __unicode__(self):
        return self.yearly

class Months(models.Model):
    monthly = models.CharField(max_length=200)

    class Meta:
        verbose_name_plural = "Months"

    def __unicode__(self):
        return self.monthly

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

class RiskOfDrought(models.Model):
    description = models.CharField(max_length=200)
    risk_of_drought_id = models.IntegerField(unique=True )

    class Meta:
        verbose_name_plural = "Risk of Drought"

    def __unicode__(self):
        return self.description

class Trends(models.Model):
    description = models.CharField(max_length=200)
    trends_id = models.IntegerField(unique=True )

    class Meta:
        verbose_name_plural = "Trends"

    def __unicode__(self):
        return self.description
        

class Indicators(models.Model):
    description = models.CharField(max_length=200)
    sector = models.ForeignKey(Sectors)
    indicator_id = models.IntegerField(unique=True)


    class Meta:
        verbose_name_plural = "Indicators"

    def __unicode__(self):
        return self.description


class Phase(models.Model):
    description = models.CharField(max_length=200)
    phase_id = models.IntegerField(unique=True)

    class Meta:
        verbose_name_plural = "Phase"

    def __unicode__(self):
        return self.description


class Report(models.Model):
    pdf = models.FileField(upload_to="reports")
    description = models.CharField(max_length=300)

    class Admin:
        list_display = ('description')

    def __unicode__(self):
        return self.description

class Documentation (models.Model):
    file = models.FileField(upload_to="docs")
    description = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "Documentation"

    class Admin:
        list_display = ('description')

    def __unicode__(self):
        return self.description

class Map(models.Model):
    image = models.FileField(upload_to="maps")
    description = models.CharField(max_length=300) 
    district = models.ForeignKey(Districts)
    month = models.ForeignKey(Months)
    year = models.ForeignKey(Years)

    class Admin:
        list_display = ('description')

    def __unicode__(self):
        return self.description   

class LivelihoodZonePhaseClassification(models.Model):
    district = models.IntegerField()
    years = models.ForeignKey(Years)
    months = models.ForeignKey(Months)
    riskofdrought = models.ForeignKey(RiskOfDrought, to_field='risk_of_drought_id')
    livelihoodzones = models.ForeignKey(LivelihoodZones)
    phase = models.ForeignKey(Phase, to_field='phase_id')
    trends = models.ForeignKey(Trends, to_field='trends_id')
    created = models.DateTimeField(auto_now_add=True)
    sequenceid = models.BigIntegerField()
    dews_created = models.DateTimeField()

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in LivelihoodZonePhaseClassification._meta.fields]



class VulnerabilityIndicators(models.Model):
    district = models.IntegerField()
    years = models.ForeignKey(Years)
    months = models.ForeignKey(Months)
    livelihoodzones = models.ForeignKey(LivelihoodZones)
    sectors = models.ForeignKey(Sectors)
    indicators =  models.ForeignKey(Indicators)
    phase = models.ForeignKey(Phase)
    datavalue = models.IntegerField(default=0)
    sequenceid = models.BigIntegerField()




   
   

      