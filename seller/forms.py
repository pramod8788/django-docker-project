from django import forms
from ecommerce import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.contrib.auth import get_user_model
from ecommerce import models


User = get_user_model()

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = models.Contact
        fields = "__all__"
        labels = {
            "full_name": "Enter Your Full Name",
            "email": "Enter Email",
            "message": "Drop the Message"
        }
        widgets = {
            "full_name": forms.TextInput(attrs={"class":"form-control"}),
            "email": forms.EmailInput(attrs={"class":"form-control"}),
            "message": forms.Textarea(attrs={"class":"form-control", "rows":3})
        }


class FashionForm(forms.ModelForm):
    class Meta:
        model = models.Fashion
        fields = "__all__"
        exclude = ("slug", "seller_name")
        labels = {
            "prod_name": "Product's Name",
            "type": "Product's Type",
            "price": "Product's Price",
            "colour": "Product's Colour",
            "size": "Product's Size (Optional)",
            "in_stock": "Product in Stock",
            "info": "Product's More Description",
            "image1": "Product's Image 1",
            "image2": "Product's Image 2",
            "image3": "Product's Image 3",
        }

        widgets = {
            'prod_name': forms.TextInput(attrs={'class':'form-control'}),
            'type': forms.Select(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'colour': forms.TextInput(attrs={'class':'form-control'}),
            'size': forms.TextInput(attrs={'class':'form-control'}),
            'in_stock': forms.NumberInput(attrs={'class':'form-control'}),
            'info': forms.Textarea(attrs={'class':'form-control', 'rows': '2'}),
            'image1': forms.FileInput(attrs={'class':'form-control'}),
            'image2': forms.FileInput(attrs={'class':'form-control'}),
            'image3': forms.FileInput(attrs={'class':'form-control'}),
        }


class MobileForm(forms.ModelForm):
    class Meta:
        model = models.Mobile
        fields = "__all__"
        exclude = ("slug", "seller_name")
        labels = {
            "prod_name": "Product's Name",
            "type": "Product's Type",
            "price": "Product's Price",
            "colour": "Product's Colour",
            "size": "Product's Size (Optional)",
            "in_stock": "Product in Stock",
            "info": "Product's More Description",
            "image1": "Product's Image 1",
            "image2": "Product's Image 2",
            "image3": "Product's Image 3",
        }

        widgets = {
            'prod_name': forms.TextInput(attrs={'class':'form-control'}),
            'type': forms.Select(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'colour': forms.TextInput(attrs={'class':'form-control'}),
            'size': forms.TextInput(attrs={'class':'form-control'}),
            'in_stock': forms.NumberInput(attrs={'class':'form-control'}),
            'info': forms.Textarea(attrs={'class':'form-control', 'rows': '2'}),
            'image1': forms.FileInput(attrs={'class':'form-control'}),
            'image2': forms.FileInput(attrs={'class':'form-control'}),
            'image3': forms.FileInput(attrs={'class':'form-control'}),
        }


class ElectronicForm(forms.ModelForm):
    class Meta:
        model = models.Electronic
        fields = "__all__"
        exclude = ("slug", "seller_name")
        labels = {
            "prod_name": "Product's Name",
            "type": "Product's Type",
            "price": "Product's Price",
            "colour": "Product's Colour",
            "size": "Product's Size (Optional)",
            "in_stock": "Product in Stock",
            "info": "Product's More Description",
            "image1": "Product's Image 1",
            "image2": "Product's Image 2",
            "image3": "Product's Image 3",
        }

        widgets = {
            'prod_name': forms.TextInput(attrs={'class':'form-control'}),
            'type': forms.Select(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'colour': forms.TextInput(attrs={'class':'form-control'}),
            'size': forms.TextInput(attrs={'class':'form-control'}),
            'in_stock': forms.NumberInput(attrs={'class':'form-control'}),
            'info': forms.Textarea(attrs={'class':'form-control', 'rows': '2'}),
            'image1': forms.FileInput(attrs={'class':'form-control'}),
            'image2': forms.FileInput(attrs={'class':'form-control'}),
            'image3': forms.FileInput(attrs={'class':'form-control'}),
        }


class HomeDecorForm(forms.ModelForm):
    class Meta:
        model = models.HomeDecor
        fields = "__all__"
        exclude = ("slug", "seller_name")
        labels = {
            "prod_name": "Product's Name",
            "type": "Product's Type",
            "price": "Product's Price",
            "colour": "Product's Colour",
            "size": "Product's Size (Optional)",
            "in_stock": "Product in Stock",
            "info": "Product's More Description",
            "image1": "Product's Image 1",
            "image2": "Product's Image 2",
            "image3": "Product's Image 3",
        }

        widgets = {
            'prod_name': forms.TextInput(attrs={'class':'form-control'}),
            'type': forms.Select(attrs={'class':'form-control'}),
            'price': forms.NumberInput(attrs={'class':'form-control'}),
            'colour': forms.TextInput(attrs={'class':'form-control'}),
            'size': forms.TextInput(attrs={'class':'form-control'}),
            'in_stock': forms.NumberInput(attrs={'class':'form-control'}),
            'info': forms.Textarea(attrs={'class':'form-control', 'rows': '2'}),
            'image1': forms.FileInput(attrs={'class':'form-control'}),
            'image2': forms.FileInput(attrs={'class':'form-control'}),
            'image3': forms.FileInput(attrs={'class':'form-control'}),
        }


class SellerSignup(UserCreationForm):
    phone_number = forms.CharField(label="Enter Phone Number", max_length=10, widget=forms.TextInput(attrs={'class':'form-control'}))
    gst_id = forms.CharField(label="Enter GSTIN", max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    aadhar_number = forms.CharField(label="Enter Aadhar Number", max_length=20, widget=forms.TextInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = [
            'username', 
            'first_name', 
            'last_name', 
            'email', 
            'password1', 
            'password2',
            ]

    def __init__(self, *args, **kwargs):
        super(SellerSignup, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs['class'] = 'form-control'
        self.fields["username"].label = "Enter Username"

        self.fields["first_name"].widget.attrs['class'] = 'form-control'
        self.fields["first_name"].label = "Enter First Name"

        self.fields["last_name"].widget.attrs['class'] = 'form-control'
        self.fields["last_name"].label = "Enter Last Name"
        
        self.fields["email"].widget.attrs['class'] = 'form-control'
        self.fields["email"].label = "Enter Email"
        
        self.fields["password1"].widget.attrs['class'] = 'form-control'
        self.fields["password1"].label = "Enter Password"
        
        self.fields["password2"].widget.attrs['class'] = 'form-control'
        self.fields["password2"].label = "Confirm Password"


class LoginForm(AuthenticationForm):
    username = UsernameField(label="Enter Username", widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label="Enter Password", widget=forms.PasswordInput(attrs={'class':'form-control'}))
    