from django_tables2_reports.tables import TableReport
import django_tables2 as tables
from Karamoja.models  import LivelihoodZonePhaseClassification



class LivelihoodZoneTable(TableReport):

    class Meta:
        model = LivelihoodZonePhaseClassification
        orderable = False
        fields = ("district", "months", "livelihoodzones", "access_to_pasture", "animals_in_good_body_condition", "disease_incidence_in_livestock", "livestock_migration", "germination_of_crops", "crops_affected_by_pests_and_diseases", "borehole_useage", "average_time_to_fetch_water", "average_water_qty_fetched_daily", "price_of_bull", "price_of_sorghum", "price_of_charcoal", "price_of_firewood", "freedom_of_movement_daytime", "freedom_of_movement_nightime", "casual_labor_rate", "gam_rate")
        
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue", 'width':'200%'}
   

class LivelihoodZoneTableAnalysis(TableReport):



    class Meta:
        model = LivelihoodZonePhaseClassification
        orderable = False
        fields = ("livelihoodzones","livestock_sector_phase", "access_to_pasture", "animals_in_good_body_condition", "disease_incidence_in_livestock", "livestock_migration", "crops_sector_phase", "germination_of_crops", "crops_affected_by_pests_and_diseases", "water_sector_phase", "borehole_useage", "average_time_to_fetch_water", "average_water_qty_fetched_daily", "livelihoods_sector_phase", "price_of_bull", "price_of_sorghum", "price_of_charcoal", "price_of_firewood", "freedom_of_movement_daytime", "freedom_of_movement_nightime", "casual_labor_rate", "gam_rate")
        
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue", 'width':'80px'}