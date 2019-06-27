from django.conf.urls import url, include
from django.contrib.auth.views import login,logout
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from django.contrib import auth
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django_filters.views import FilterView
from triptricks.views import model_form_upload, create_new_travel_plan, edit_travel_plan, list_travel_contents
from triptricks.filters import PlanFilter

from django.views.generic.base import RedirectView    
favicon_view = RedirectView.as_view(url='/static/favicon.ico', permanent=True)

urlpatterns = [
    url(r'^favicon\.ico$', favicon_view),
    url(r'^$', views.index, name='index'),
    # Login page
    url(r'^login/$', login, {'template_name': 'triptricks/login.html'},  name='login'),
    # Logout page
    url(r'^logout/$', views.logout_view, name='logout'),
    #url(r'^logged_out/$',{'template_name': 'triptricks/logged_out.html'},  name='loggedout'),
    url(r'^new_user_registeration/$', views.register, name='register'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^afterlogin/$', views.after_login, name='afterlogin'),
    url(r'^alogin/$', FilterView.as_view(filterset_class=PlanFilter,template_name='triptricks/afterLogin.html.html'), name='search'),
    url(r'^loggedout/$', views.loggedout,  name='loggedout'),    
   
    
    #url(r'^reset/$', views.reset, name='reset' ),
    #url(r'^password_reset_done/$', auth_views.password_reset_done, name='password_reset_done'),
    #url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', views.reset_confirm, name='password_reset_confirm' ),
    url(r'^password_reset/$', auth_views.password_reset, 
        {'post_reset_redirect' : '/password_reset/done/'}, name='password_reset'),
    url(r'^password_reset/done/$', auth_views.password_reset_done),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', auth_views.password_reset_confirm, 
        {'post_reset_redirect' : '/reset/done/'}),
    url(r'^reset/done/$', auth_views.password_reset_complete, name='password_reset_complete'),  
    
    url(r'^password/$', views.change_password, name='change_password'),
    url(r'^password/changed$', views.change_password_done, name='change_password_done'),
    url(r'^upload_pic/$', views.model_form_upload, name='upload_pic'),
    url(r'^deleteimage/(?P<id>\d+)/$', views.delete_image, name='deleteimage'),
    url(r'^createnewplan/$', views.create_new_travel_plan, name='createnewplan'),
    url(r'^edittravelplan/(?P<id>\d+)/$', views.edit_travel_plan, name='edittravelplan'),
    url(r'^viewtravelplan/$', views.view_travel_plan, name='viewtravelplan'),
    url(r'deleteplan/(?P<id>\d+)/$', views.delete_travel_plan, name='deletetravelplan'),
    url(r'searchplan/$', views.search_travel_plan, name='searchtravelplan'),
    url(r'listtravelcontent/(?P<id>\d+)/$', views.list_travel_contents, name='listtravelcontents'),
    
]    
