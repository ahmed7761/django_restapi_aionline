from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta:
              model = Customer
              fields = "__all__"

    gender = forms.TypedChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
    age = forms.IntegerField()
    salary = forms.IntegerField()

