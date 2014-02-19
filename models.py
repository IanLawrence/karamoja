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
        return u"%s" % self.yearly

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
    district = models.ForeignKey(Districts)
    month = models.ForeignKey(Months)
    year = models.ForeignKey(Years)

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
    district = models.ForeignKey(Districts, to_field='district_id')
    years = models.ForeignKey(Years)
    months = models.ForeignKey(Months)
    riskofdrought = models.ForeignKey(RiskOfDrought, to_field='risk_of_drought_id')
    livelihoodzones = models.ForeignKey(LivelihoodZones)
    phase = models.ForeignKey(Phase, to_field='phase_id')
    trends = models.ForeignKey(Trends, to_field='trends_id')
    created = models.DateTimeField(auto_now_add=True)
    sequenceid = models.BigIntegerField()
    dews_created = models.DateTimeField()
    livestock_sector_phase = models.ForeignKey(Phase, to_field='phase_id', related_name='livestock_sector_phase')
    crops_sector_phase = models.ForeignKey(Phase, to_field='phase_id', related_name='crops_sector_phase')
    water_sector_phase = models.ForeignKey(Phase, to_field='phase_id', related_name='water_sector_phase')
    livelihoods_sector_phase = models.ForeignKey(Phase, to_field='phase_id', related_name='livelihoods_sector_phase')
    access_to_pasture = models.FloatField()
    animals_in_good_body_condition = models.FloatField()
    disease_incidence_in_livestock = models.FloatField()
    livestock_migration = models.FloatField()
    germination_of_crops = models.FloatField()
    crops_affected_by_pests_and_diseases = models.FloatField()
    borehole_useage  = models.FloatField()
    average_time_to_fetch_water = models.FloatField()
    average_water_qty_fetched_daily = models.FloatField()
    price_of_bull = models.FloatField()
    price_of_sorghum = models.FloatField()
    price_of_charcoal = models.FloatField()
    price_of_firewood = models.FloatField()
    freedom_of_movement_daytime = models.FloatField()
    freedom_of_movement_nightime = models.FloatField()
    casual_labor_rate = models.FloatField()
    gam_rate = models.FloatField()


    def __unicode__(self):
       return unicode(self.created) or u''



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




   
   

      