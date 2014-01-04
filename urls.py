from django.conf.urls import patterns, url
from django.conf import settings


from Karamoja import views

urlpatterns = patterns('',
    url(r'^$', views.jsonit, name='jsonit'),
    url(r'^save_livelihood_data/', views.save_livelihood_data, name='save_livelihood_data'),
    url(r'^save_vulnerability_data/', views.save_vulnerability_data, name='save_vulnerability_data')
) 


