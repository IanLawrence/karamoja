from django_tables2_reports.tables import TableReport
from Karamoja.models  import LivelihoodZonePhaseClassification

class LivelihoodZoneTable(TableReport):
    class Meta:
        model = LivelihoodZonePhaseClassification
        fields = ("district", "months", "livelihoodzones", "access_to_pasture", "animals_in_good_body_condition", "disease_incidence_in_livestock", "livestock_migration", "germination_of_crops", "crops_affected_by_pests_and_diseases", "borehole_useage", "average_time_to_fetch_water", "average_water_qty_fetched_daily", "price_of_bull", "price_of_sorghum", "price_of_charcoal", "price_of_firewood", "freedom_of_movement_daytime", "freedom_of_movement_nightime", "casual_labor_rate", "gam_rate")
        
        # add class="paleblue" to <table> tag
        attrs = {"class": "paleblue", 'width':'200%'}