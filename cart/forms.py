from django import forms
from cart.cart import Cart
from django.shortcuts import render, redirect, get_object_or_404
from item.models import Item

class CartAddItemForm(forms.Form):
    item_id = forms.IntegerField()
    quantity = forms.IntegerField()
    update = forms.IntegerField() 
