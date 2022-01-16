from django.shortcuts import render, redirect
from inventory_register.form import InventoryForm
from inventory_register.models import Inventory
from PIL import Image
import os

def inventory_list(request):
    """Show the inventory list"""
    context = {'inventory_list': Inventory.objects.all()}
    return render(request, "inventory_register/inventory_list.html", context)

def inventory_form(request, id=0):
    """Show the inventory form"""
    if request.method == "GET":
        if id == 0:
            form = InventoryForm()
        else:
            inventory = Inventory.objects.get(pk = id)
            form = InventoryForm(instance = inventory)
        return render(request, "inventory_register/inventory_form.html", {'form':form})
    else:
        if id == 0:
            form = InventoryForm(request.POST, request.FILES)
        else:
            inventory = Inventory.objects.get(pk=id)
            form = InventoryForm(request.POST, request.FILES, instance = inventory)
        if form.is_valid():
            form.save()
        return redirect('/inventory/list')

def inventory_delete(request, id):
    """ Delete the item"""
    inventory = Inventory.objects.filter(pk=id)
    inventory.delete()
    return redirect('/inventory/list')
