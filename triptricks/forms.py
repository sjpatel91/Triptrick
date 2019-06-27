from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from triptricks.models import Document, Plan




class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    password1 = forms.CharField(widget=forms.PasswordInput, help_text='Your password cannnot be too similar to your other personal information.Your password must contain at least 8 characters.Your password cannnot be a commonly used password.Your password cannot be entirely numeric.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
        
class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('description', 'document', )

class PlanForm(forms.ModelForm):
    
    class Meta:
        model = Plan
        fields = {'destination_name', 'number_days', 'sub_destination', 'description',}
        
        label = {'destination_name':'Destination', 'number_days':'Days', 'sub_destination':'SubDestination', 'description':'Description',}
        widgets = {'destination_name': forms.TextInput(attrs=
                                                       {'class':'form-control','placeholder':'please give destination name', 'id':'geocomplete'}), 
                                                       'number_days':forms.TextInput(attrs={'class':'form-control','placeholder':'please enter the total number of days your trip took'}), 
                                                       'sub_destination':forms.TextInput(attrs={'class':'form-control','placeholder':'please enter the sub destinations',
                                                       'data-role':"tagsinput"}), 'description':forms.Textarea(attrs={'class':'form-control'}),}
 
class SearchPlan(forms.Form):
    #search = forms.CharField(label='search',  widget=forms.TextInput(attrs={'placeholder': 'Search'}))
    search_t = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder': 'Search'}))
    
        