from django import forms
from django.core import validators

def Check_For_Z(value):
    if value[0].lower()!='s':
        raise forms.ValidationError("Name should start with Z")


    
    
class FormName(forms.Form):
    name=forms.CharField(validators=[Check_For_Z])
    email=forms.EmailField()
    verify_email=forms.EmailField(label="enter email again")
    text=forms.CharField(widget=forms.Textarea)
    botcatcher=forms.CharField(required=False,widget=forms.HiddenInput,validators=[validators.MaxLengthValidator(0)])
    
    def clean(self):
        all_clean_data=super().clean()
        email=all_clean_data['verify_email']
        vemail=all_clean_data['email']
        
        if(email!=vemail):
            raise forms.ValidationError("make sure that the email correct")
        