from items.models import item
from django import forms 

class itemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ("name", 'discription', 'price', 'categoty', 'image')
        
        
class EdititemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ("name", 'discription', 'price', 'categoty', 'image', 'is_sold')
            