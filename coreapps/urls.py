# Overview
#
# A view is a “type” of Web page in your Django application that generally serves a specific function and has a
# specific template. For example, in a blog application, you might have the following views:
#
    # By Places
    # By Departments
    # By Companies
    # By Things
    # By Kb Articles
    # By Notes
    # By Links

    # Oncall page
        # should show our servicenow incidents
        # our jira tasks
        # various systems blocks with support site, confluence, jira, servicenow, etc.

    # Blog homepage – displays the latest few entries.
    # Entry “detail” page – permalink page for a single entry.
    # Year-based archive page – displays all months with entries in the given year.
    # Month-based archive page – displays all days with entries in the given month.
    # Day-based archive page – displays all entries in the given day.
    # Comment action – handles posting comments to a given entry.
#
# In our poll application, we’ll have the following four views:
#
    # Question “index” page – displays the latest few questions.
    # Question “detail” page – displays a question text, with no results but with a form to vote.
    # Question “results” page – displays results for a particular question.
    # Vote action – handles voting for a particular choice in a particular question.
#
# In Django, web pages and other content are delivered by views. Each view is represented by a simple Python
# function (or method, in the case of class-based views). Django will choose a view by examining the URL that’s
# requested (to be precise, the part of the URL after the domain name).
#
# Now in your time on the web you may have come across such beauties as
# “ME2/Sites/dirmod.asp?sid=&type=gen&mod=Core+Pages&gid=A6CD4967199A42D9B65B1B”. You will be pleased to
# know that Django allows us much more elegant URL patterns than that.
#
# A URL pattern is simply the general form of a URL - for example: /newsarchive/<year>/<month>/.
#
# To get from a URL to a view, Django uses what are known as ‘URLconfs’. A URLconf maps URL patterns
# (described as regular expressions) to views.

from django.conf.urls import url
from . import views

app_name = 'coreapps'

urlpatterns = [
    # ex: /coreapps/
    url(r'^$', views.index, name='index'),
    url(r'^lifecycle/$', views.lifecycle_home, name='lifecycle_home'),
    url(r'^department/$', views.departments_home, name='departments_home'),
    url(r'^departments_import/$', views.departments_import, name='departments_import'),
    url(r'^department_form/$', views.department_form, name='department_form'),
    url(r'^department/(?P<department_id>[0-9]+)/detail$', views.department_detail, name='department_detail'),
    url(r'^company/$', views.companies_home, name='companies_home'),
    url(r'^company_form/$', views.company_form, name='company_form'),
    url(r'^company/(?P<company_id>[0-9]+)/detail$', views.company_detail, name='company_detail'),
    url(r'^things/$', views.things_home, name='things_home'),
    url(r'^thing_form/$', views.thing_form, name='thing_form'),
    url(r'^thing/(?P<thing_id>[0-9]+)/detail$', views.thing_detail, name='thing_detail'),
    url(r'^kbs/$', views.kbs_home, name='kbs_home'),
    url(r'^kb_form/$', views.kb_form, name='kb_form'),
    url(r'^kb/(?P<kb_id>[0-9]+)/detail$', views.kb_detail, name='kb_detail'),
    url(r'^notes/$', views.notes_home, name='notes_home'),
    url(r'^note_form/$', views.note_form, name='note_form'),
    url(r'^note/(?P<note_id>[0-9]+)/detail$', views.note_detail, name='note_detail'),
    url(r'^links/$', views.links_home, name='links_home'),
    url(r'^link_form/$', views.link_form, name='link_form'),
    url(r'^link/(?P<link_id>[0-9]+)/detail$', views.link_detail, name='link_detail'),
    url(r'^groups/$', views.groups_home, name='groups_home'),
    url(r'^group_form/$', views.group_form, name='group_form'),
    url(r'^group_form/(?P<group_id>[0-9]+)$', views.group_form, name='group_form'),
    url(r'^group/(?P<group_id>[0-9]+)/detail$', views.group_detail, name='group_detail'),
    url(r'^places/$', views.places_home, name='places_home'),
    url(r'^places_import/$', views.places_import, name='places_import'),
    url(r'^place_form/$', views.place_form, name='place_form'),
    url(r'^place/(?P<place_id>[0-9]+)/detail/$', views.place_detail, name='place_detail'),
]
