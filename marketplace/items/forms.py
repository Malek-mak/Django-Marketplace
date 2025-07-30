from items.models import item, Review
from django import forms 

class itemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ("name", 'discription', 'price', 'categoty', 'image')
        
        
class EdititemForm(forms.ModelForm):
    class Meta:
        model = item
        fields = ("name", 'discription', 'price', 'categoty', 'image', 'is_sold')


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating', 'comment')
        
    
    comment = forms.CharField(widget=forms.TextInput(attrs={'class': 'w-full rounded-xl py-6 px-12 border', 'placeholder': 'Enter your Review...'}))