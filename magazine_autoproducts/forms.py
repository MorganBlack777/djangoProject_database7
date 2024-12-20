from .models import Autoproduct
from django import forms
from .models import Store

class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = ['Store_name', 'URL', 'Description']

class AutoproductForm(forms.ModelForm):
    class Meta:
        model = Autoproduct
        fields = ['Autoproduct_type', 'Price', 'In_stock_size', 'Material', 'Color', 'Weight', 'Size', 'ID_store', 'Autoproduct_photo']
