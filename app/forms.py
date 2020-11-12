
from django import forms
from .models import CustomUser

class mypageForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ('first_name', 'last_name', 'username', 'email', 'country', 'state', 'zipnumber', 'address1', 'address2')
    
    def __str__(self) : 
        return self.username