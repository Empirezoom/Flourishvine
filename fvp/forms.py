from django import forms 
from .models import Contact,Comment,CompanyProfile,Activity,Testimonies,AdminInfo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from userprofile.models import Member

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact 
        fields = ['full_name','email', 'message']
    

class MemberForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password1', 'password2', 'is_staff']     

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['first_name', 'last_name', 'email','address','phone','pix']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = '__all__'
        exclude = ['commenter','post','status']

class CompanyProfileForm(forms.ModelForm):
    class Meta:
       model = CompanyProfile
       fields = ['montheme']
    
class ActivityForm(forms.ModelForm):
    title = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    active = forms.ImageField(label='upload an image')
    content = forms.CharField(widget=forms.Textarea(attrs={'row': 4,'cols':40}))
    class Meta:
      model = Activity
      fields = ['title','active','content']

class TestimoniesForm(forms.ModelForm):
    testifier = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    passport = forms.ImageField(label='upload an image')
    testimony = forms.CharField(widget=forms.Textarea(attrs={'row': 4,'cols':40}))
    class Meta:
      model = Testimonies
      fields = ['testifier','passport','testimony']

class AdminInfoForm(forms.ModelForm):
    class Meta:
        model = AdminInfo
        fields = ['the_info']  