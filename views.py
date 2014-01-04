# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render_to_response, render, get_object_or_404 
import json
from django.conf import settings   
from django.http import Http404
from django.template import Template, Context
from django.core.context_processors import csrf
from django.utils import simplejson
from django.template import RequestContext
from django.http import HttpResponseServerError, HttpResponseRedirect
from django.core import serializers
from Karamoja.models import LivelihoodZonePhaseClassification, Districts, Years, Months, LivelihoodZones, Trends, Report, Map
from django.core.urlresolvers import reverse
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Max


def jsonit(request):
    return render_to_response('Karamoja/json.html', context_instance=RequestContext(request))

def index(request):
    return render(request, 'Karamoja/index.html')

def reports(request):
    reports_list = Report.objects.all()
    context = {'reports_list': reports_list}
    return render(request, 'Karamoja/reports.html', context)

def home(request):
    district_list = Districts.objects.all().order_by('name')
    context = {'district_list': district_list}
    return render(request, 'Karamoja/home.html', context)

def years(request, district_id):
    years_list = Years.objects.all()
    return render(request, 'Karamoja/years.html', {'years_list': years_list })

def months(request, district_id, id):
    months_list = Months.objects.all()
    return render(request, 'Karamoja/months.html', {'months_list': months_list })

def analysis(request, district_id, id, livelihoodzone):
    try:
        where = Districts.objects.get( district_id = district_id)
    except Districts.DoesNotExist:
        where = None
    try:
        imagemap = Map.objects.get(district = where.id, year = id, month = livelihoodzone)
    except Map.DoesNotExist:
        imagemap = None
    try:
        year = Years.objects.get(id = id)
    except Years.DoesNotExist:
        year = None
    try:
        month = Months.objects.get( id = livelihoodzone) 
    except Months.DoesNotExist:
        month = None
    
    try:
        pastoral = LivelihoodZonePhaseClassification.objects.filter(district=district_id, years=id, months=livelihoodzone, livelihoodzones=1).order_by('dews_created').reverse()[:1]
        agropastoral = LivelihoodZonePhaseClassification.objects.filter(district=district_id, years=id, months=livelihoodzone, livelihoodzones=2).order_by('dews_created').reverse()[:1]
        agricultural = LivelihoodZonePhaseClassification.objects.filter(district=district_id, years=id, months=livelihoodzone, livelihoodzones=3).order_by('dews_created').reverse()[:1]
    except LivelihoodZonePhaseClassification.DoesNotExist:
        raise Http404   
    return render(request, 'Karamoja/report.html', {'pastoral': pastoral, 'agropastoral': agropastoral, 'agricultural': agricultural, 'where': where, 'year': year, 'month': month, 'imagemap' : imagemap })

@csrf_exempt
def save_livelihood_data(request):
  if request.method == 'POST':
    jsondata = request.body
    final = json.loads(jsondata)
    print final

    # Iterate through the stuff in the json
    try:
    	for key, value in final.iteritems():
            print key
        if type(value) == type(['']):
            for sub_value in value:
            	    obj, created = LivelihoodZonePhaseClassification.objects.get_or_create(**sub_value)
            	    if created == False:
            	    	break       	                            
        else:
        	 pass

    except KeyError:
        HttpResponseServerError("Malformed data!")
    
  return HttpResponse("Thanks")

@csrf_exempt
def save_vulnerability_data(request):
  if request.method == 'POST':
    jsondata = request.body
    final = json.loads(jsondata)

    # Iterate through the stuff in the json
    try:
    	for key, value in final.iteritems():
            print key
        if type(value) == type(['']):
            for sub_value in value:
            	    obj, created = VulnerabilityIndicators.objects.get_or_create(**sub_value)
            	    if created == False:
            	    	break      	                            
        else:
        	 pass

    except KeyError:
        HttpResponseServerError("Malformed data!")
    
  return HttpResponse("Thanks")


    
