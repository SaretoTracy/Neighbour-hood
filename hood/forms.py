from django.contrib.auth.models import User
from django import forms
from .models import Profile,NeighbourHood,Business,Post

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields=['profile_picture','bio','email','phone_no'] 
class HoodForm(forms.ModelForm):
    class Meta:
        model = NeighbourHood
        fields=['name','location','description','image']         
        
class BusinessForm(forms.ModelForm):
    class Meta:
        model = Business
        fields=['image','name','email','phone_no']            

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields=['title','info']       
       