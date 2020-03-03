from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

COLLEGE_CHOICES = [
    ('IIITS', 'IITS'),
    ('IITK', 'IIIK'),
    ('IITM', 'IIIM'),
]
class SignupForm(UserCreationForm):
    email = forms.EmailField()
    institution_id = forms.CharField(max_length=100 )
    college = forms.CharField(
        max_length=13,
        widget=forms.Select(choices=COLLEGE_CHOICES),
    )
   
     
    class Meta:
        model = User
        fields = ['username', 'email', 'institution_id','college']
        
       