from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.core.exceptions import ValidationError
from . import models


User = get_user_model()

class AddressForm(forms.ModelForm):
    class Meta:
        model = models.Address
        fields = "__all__"
        exclude = ["user"]

        labels = {
            "full_name": "Full Name",
            "phone_num": "Phone Number",
            "building_num_name": "House/Building/Flat - Number and Name",
            "area_colony": "Road/Street/Colony/Area",
            "landmark": "Nearby Landmark (Optional)",
            "pincode": "Pincode",
            "city": "City",
            "state": "State",
            "address_type": "Address Type",
        }

        widgets = {
            'full_name': forms.TextInput(attrs={'class':'form-control'}),
            'phone_num': forms.TextInput(attrs={'class':'form-control'}),
            'building_num_name': forms.TextInput(attrs={'class':'form-control'}),
            'area_colony': forms.TextInput(attrs={'class':'form-control'}),
            'landmark': forms.TextInput(attrs={'class':'form-control'}),
            'pincode': forms.NumberInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'state': forms.TextInput(attrs={'class':'form-control'}),
            'address_type': forms.Select(attrs={'class':'form-control'}),
        }


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


class LoginForm(AuthenticationForm):
    username = UsernameField(label='Enter Username', widget=forms.TextInput(attrs={'class':'form-control'}))
    password = forms.CharField(label='Enter Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    def confirm_login_allowed(self, user):
        if user.is_staff and not user.is_superuser:
            raise ValidationError(
                ("This account is not allowed here."),
                code='inactive',
            )


class ModifiedUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


    def __init__(self, *args, **kwargs):
        super(ModifiedUserForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs['class'] = 'form-control'
        self.fields["username"].widget.attrs['autofocus'] = False
        self.fields["username"].label = "Enter Username"

        self.fields["first_name"].widget.attrs['class'] = 'form-control'
        self.fields["first_name"].widget.attrs['autofocus'] = True
        self.fields["first_name"].label = "Enter First Name"

        self.fields["last_name"].widget.attrs['class'] = 'form-control'
        self.fields["last_name"].label = "Enter Last Name"
        
        self.fields["email"].widget.attrs['class'] = 'form-control'
        self.fields["email"].label = "Enter Email"
        
        self.fields["password1"].widget.attrs['class'] = 'form-control'
        self.fields["password1"].label = "Enter Password"
        
        self.fields["password2"].widget.attrs['class'] = 'form-control'
        self.fields["password2"].label = "Confirm Password"