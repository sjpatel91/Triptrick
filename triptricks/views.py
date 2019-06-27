# -*- coding: utf-8 -*-
#from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.core.urlresolvers import reverse
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm
from triptricks.forms import SignUpForm
from django.contrib.sessions.models import Session
from django.contrib import auth

from django.core.urlresolvers import reverse
from django.contrib.auth.views import password_reset, password_reset_confirm

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect, get_object_or_404

from django.conf import settings
from django.core.files.storage import FileSystemStorage
from triptricks.forms import  DocumentForm, PlanForm, SearchPlan
from triptricks.models import Document, Plan
from triptricks.filters import PlanFilter


def index(request):
    #template = loader.get_template('triptricks/index.html')
    return render(request, 'triptricks/index.html')
   
'''def signin(request):
    return render(request, 'triptricks/signin.html')'''
def register(request):
    """Register a new user."""
    if request.method != 'POST':
        # Display blank registration form.
        form = SignUpForm()
    else:
        # Process completed form.
        #form = UserCreationForm(data=request.POST)
        form = SignUpForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            username = form.cleaned_data.get('username')
            password1 = form.cleaned_data.get('password1')
            # Log the user in and then redirect to home page.
            authenticated_user = authenticate(username=new_user.username,
            password=password1)
            login(request, authenticated_user)
            return HttpResponseRedirect(reverse('triptricks:profile'))
    context = {'form': form}
    return render(request, 'triptricks/register.html', context)
    #return render(request, 'triptricks/register.html')
def profile(request):
    if not request.user.is_authenticated():
        #return render(request, 'triptricks/logged_out.html')
        return HttpResponseRedirect(reverse('triptricks:loggedout'))
    else:
        profile_form = DocumentForm()
        profile_images=Document.objects.filter(owner_id = request.user.id)
        
        profile_plan_form = PlanForm()
        profile_plan = Plan.objects.filter(owner_id = request.user.id)
        
        if len(profile_images) > 6: 
            profile_images = profile_images[:6]
        if len(profile_plan) > 8:
            profile_plan = profile_plan[:8]
            
        total_images = len(profile_images)
        total_plan = len(profile_plan)
        
        plan_list = Plan.objects.all()
        plan_filter = PlanFilter(request.GET, queryset=plan_list)
        
                                
                                
        return render(request, 'triptricks/profile.html', {
            'profile_form': profile_form, 'profile_images':profile_images, 'profile_plan_form':profile_plan_form, 'profile_plan':profile_plan, 
            'total_images': total_images, 'total_plan': total_plan , 'filter': plan_filter
        })  
        #return render(request, 'triptricks/profile.html') 
        
def after_login(request):
    if not request.user.is_authenticated():
        #return render(request, 'triptricks/logged_out.html')
        return HttpResponseRedirect(reverse('triptricks:loggedout'))
    else:
        trick_search_form = SearchPlan()
        plan_all_list = Plan.objects.all()
        plan_all_filter = PlanFilter(request.GET, queryset=plan_all_list)
        return render(request, 'triptricks/afterLogin.html', {
            'search_form': trick_search_form , 'filter_all': plan_all_filter
            }) 

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse('triptricks:index'))
def loggedout(request):
    
    return render(request, 'triptricks/logged_out.html')

'''def password_reset_confirm(request, uidb64=None, token=None):
    return password_reset_confirm(request, template_name='triptricks/registration/password_reset_confirm.html',
        uidb64=uidb64, token=token, post_reset_redirect=reverse('triptricks:login'))


def reset(request):
    return password_reset(request, template_name='triptricks/registration/password_reset_form.html',
        email_template_name='triptricks/registration/password_reset_email.html',
        subject_template_name='triptricks/registration/password_reset_subject.txt',
        post_reset_redirect='triptricks/registration/password_reset_done.html') ''' 

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            #messages.success(request, 'Your password was successfully updated!')
            return redirect('triptricks:change_password_done')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'triptricks/registration/change_password.html', {
        'form': form
    })
    
def change_password_done(request):
    return render(request, 'triptricks/registration/change_password_done.html')



def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = form.save(commit=False)
            new_image.owner = request.user
            new_image.save()
            
            #return HttpResponse('Trip image upload success')
            messages.success(request, 'Trip image upload success.')
        return redirect('triptricks:upload_pic')
        
    else:
        form = DocumentForm()
        images=Document.objects.all()
        
   
    return render(request, 'triptricks/upload_pic.html', {
        'form': form, 'images':images
    })
def delete_image(request, id):
    image = Document.objects.get(pk=id).delete()
    if request.get_full_path() == 'triptricks/upload_pic.html':
        return HttpResponseRedirect(reverse('triptricks:upload_pic')) 
    else:
        return HttpResponseRedirect(reverse('triptricks:profile'))

def create_new_travel_plan(request):
    if request.method != 'POST':
        form_plan = PlanForm()
        plan_entry = Plan.objects.all()
    else:
        form_plan = PlanForm(request.POST)
        
        if form_plan.is_valid():
           new_plan = form_plan.save(commit=False)
           new_plan.owner = request.user
           new_plan.save()
            
        return redirect('triptricks:createnewplan')
    
    context_plan = {'form' : form_plan, 'plan_entry' : plan_entry}          
    return render(request, 'triptricks/create_new_travel_plan.html', context_plan)

def edit_travel_plan(request, id):
    post = get_object_or_404(Plan, pk=id)
    if request.method == "POST":
        form = PlanForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            
            post.save()
            return redirect('triptricks:viewtravelplan')
    else:
        form = PlanForm(instance=post)
    return render(request, 'triptricks/edit_travel_plan.html', {'form': form})
    
   
    

def view_travel_plan(request):
    if not request.user.is_authenticated():
        #return render(request, 'triptricks/logged_out.html')
        return HttpResponseRedirect(reverse('triptricks:loggedout'))
    else:
                
        view_plan_form = PlanForm()
        view_plan = Plan.objects.all()
                              
        return render(request, 'triptricks/view_travel_plans.html', {
            'view_plan_form':view_plan_form, 'view_plan':view_plan
        }) 
 
def delete_travel_plan(request, id):  
    delete_plan = Plan.objects.get(pk=id).delete()
    if request.get_full_path() == 'triptricks/view_travel_plans.html':
        return HttpResponseRedirect(reverse('triptricks:viewtravelplan')) 
    else:
        return HttpResponseRedirect(reverse('triptricks:viewtravelplan'))
    
def search_travel_plan(request):
    plan_list = Plan.objects.all()
    plan_filter = PlanFilter(request.GET, queryset=plan_list)
    return render(request, 'triptricks/search_plan_list.html', {'filter': plan_filter})

def list_travel_contents(request,id):
    if not request.user.is_authenticated():
        #return render(request, 'triptricks/logged_out.html')
        return HttpResponseRedirect(reverse('triptricks:loggedout'))
    else:
                
        list_post = get_object_or_404(Plan, pk=id)
        
                              
    return render(request, 'triptricks/list_travel_contents.html', {'list_plan':list_post
            
        }) 


    

    