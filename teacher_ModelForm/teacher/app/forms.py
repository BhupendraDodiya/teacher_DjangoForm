from django import forms
from .models import Teacher

class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name','age','dob','gender','hobby','image']
        labels = {'name':'NAME','dob':'DOB','age':'AGE','gender':'GENDER','hobby':'HOBBY','image':'IMAGE'}
        widgets = {'name':forms.TextInput(attrs={'placeholder':'Enter Name','autofocus':True,'class':'form-control'}),
                   'dob':forms.DateInput(attrs={'type':'date','placeholder':'Enter DOB','class':'form-control'}),
                   }
        
class TeacherUpdateForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['name','age','dob','gender','hobby']
        labels = {'name':'NAME','dob':'DOB','age':'AGE','gender':'GENDER','hobby':'HOBBY'}
        widgets = {'name':forms.TextInput(attrs={'placeholder':'Enter Name','autofocus':True,'class':'form-control'}),
                   'dob':forms.DateInput(attrs={'type':'date','placeholder':'Enter DOB','class':'form-control'}),
                   }
        

        