from django import forms
from inventory_register.models import Inventory

class InventoryForm(forms.ModelForm):

    class Meta:
        model = Inventory
        fields = ('itemname', 'quantity', 'image')
        labels ={
            'itemname': 'Item Name',
            'quantity': 'Quantity',
        }

    def __init__(self, *args, **kwargs):
        super(InventoryForm, self).__init__(*args, **kwargs)
        self.fields['image'].required = False
