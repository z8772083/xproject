from django import forms
from rbac import models

class UserForm(forms.ModelForm):

    class Meta:

        model = models.User
        fields = '__all__'

        widgets={
            'name':forms.TextInput(attrs={'class':'form-control'}),
            'age': forms.TextInput(attrs={'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control'}),
            'role':forms.Select(attrs={'class': 'form-control'}),

        }
