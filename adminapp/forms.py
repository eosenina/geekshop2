from django import forms
from django.forms import ModelForm

from authapp.forms import UserRegisterForm, UserProfileForm
from authapp.models import User
from mainapp.models import ProductCategory, Product


class UserAdminRegisterForm(UserRegisterForm):
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'image', 'first_name', 'last_name', 'image')


class UserAdminProfileForm(UserProfileForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control py-4'}))


class CategoriesAdminForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))

    class Meta:
        model = ProductCategory
        fields = ('name', 'description')


class ProductAdminForm(ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    description = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control py-4'}))
    price = forms.FloatField(widget=forms.NumberInput(attrs={'class': 'form-control py-4'}))
    quantity = forms.DecimalField(widget=forms.NumberInput(attrs={'class': 'form-control py-4'}))
    category = forms.ModelChoiceField(queryset=ProductCategory.objects.all(),
                                      widget=forms.Select(attrs={'class': 'form-control py-4'}))
    image = forms.ImageField(widget=forms.FileInput(attrs={'class': 'custom-file-input'}), required=False)

    class Meta:
        model = Product
        fields = ('name', 'image', 'description', 'price', 'quantity', 'category')
