#!/usr/bin/env python
# vim: ai ts=4 sts=4 et sw=4

from django.conf.urls.defaults import *

urlpatterns = patterns('',

    url(r'^dashboard/$',
        "logistics_project.apps.malawi.views.dashboard",
        name="malawi_dashboard"),
    url(r'^places/$',
        "logistics_project.apps.malawi.views.places",
        name="malawi_places"),
    url(r'^contacts/$',
        "logistics_project.apps.malawi.views.contacts",
        name="malawi_contacts"),
    url(r'^hsas/$',
        "logistics_project.apps.malawi.views.hsas",
        name="malawi_hsas"),
    url(r'^hsa/(?P<code>\d+)/$',
        "logistics_project.apps.malawi.views.hsa",
        name="malawi_hsa"),
    url(r'^deactivate/(?P<pk>\d+)/$',
         "logistics_project.apps.malawi.views.deactivate_hsa",
        name="deactivate_hsa"),
     url(r'^reactivate/(?P<code>\d+)/(?P<name>.+)/$',
         "logistics_project.apps.malawi.views.reactivate_hsa",
        name="reactivate_hsa"),
    url(r'^help/$',
        "logistics_project.apps.malawi.views.help",
        name="malawi_help"),
    url(r'^status/$',
        "logistics_project.apps.malawi.views.status",
        name="malawi_status"),
    url(r'^airtel-users/$',
        "logistics_project.apps.malawi.views.airtel_numbers",
        name="malawi_airtel"),
    url(r'^register-hsa/$',
        "logistics_project.apps.malawi.views.register_user",
        name="malawi_hsa"),
    url(r'^scmgr/receiver/$',
        "logistics_project.apps.malawi.views.scmgr_receiver",
        name="malawi_scmgr_receiver"),
    url(r'^facilities/$',
        "logistics_project.apps.malawi.views.facilities",
        name="malawi_facilities"),
    url(r'^facilities/(?P<code>\d+)/$',
        "logistics_project.apps.malawi.views.facility",
        name="malawi_facility"),
    url(r'^products/$',
        "logistics_project.apps.malawi.views.products",
        name="malawi_products"),
    url(r'^monitoring/$',
        "logistics_project.apps.malawi.views.monitoring",
        name="malawi_monitoring"),
    url("^monitoring/(?P<report_slug>[\w_]+)/$", 
        "logistics_project.apps.malawi.views.monitoring_report",
        name="malawi_monitoring_report")
) 




