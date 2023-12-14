from .models import Product
from django.forms import ModelForm, TextInput


class   ProductForm(ModelForm):
    class Meta:
        model = Product
        fields=['name','author','price']


        widgets = {
            "name": TextInput(attrs={
                'id': 'name',
                'placeholder' : 'Название'
            }),"author": TextInput(attrs={
                'id': 'author',
                'placeholder' : 'Автор'
            }),"price" : TextInput(attrs={
                'id': 'price',
                'placeholder': 'Цена'
            }),


        }