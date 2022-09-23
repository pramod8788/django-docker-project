from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views import generic
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, DeleteView
from ecommerce import models
from . import forms


User = get_user_model()

class Home(generic.ListView):
    template_name = "seller/home.html"
    model = models.Category
    context_object_name = "category"


class SellerSignupView(CreateView):
    form_class = forms.SellerSignup
    template_name = 'seller/seller_signup.html'
    success_url = '/seller'
    model = User

    def form_valid(self, form):
        data = super(SellerSignupView, self).form_valid(form)
        phone, gst, aadhar = form.cleaned_data.get('phone_number'), form.cleaned_data.get('gst_id'), form.cleaned_data.get('aadhar_number')
        models.Seller.objects.create(user=self.object, phone_number=phone, gst_id=gst,aadhar_number=aadhar)
        
        self.object.is_staff = True
        self.object.groups.add(1)
        self.object.save()
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return data


class ElectronicUploadView(CreateView):
    form_class = forms.ElectronicForm
    template_name = 'seller/seller_upload.html'
    success_url = "/seller/"

    def form_valid(self, form):
        valid = super(ElectronicUploadView, self).form_valid(form)
        seller = models.Seller.objects.get(user=self.request.user)
        self.object.seller_name = seller
        self.object.save()
        return valid


class FashionUploadView(CreateView):
    form_class = forms.FashionForm
    template_name = 'seller/seller_upload.html'
    success_url = "/seller/"

    def form_valid(self, form):
        valid = super(FashionUploadView, self).form_valid(form)
        seller = models.Seller.objects.get(user=self.request.user)
        self.object.seller_name = seller
        self.object.save()
        return valid


class HomeDecoreUploadView(CreateView):
    form_class = forms.HomeDecorForm
    template_name = 'seller/seller_upload.html'
    success_url = "/seller/"

    def form_valid(self, form):
        valid = super(HomeDecoreUploadView, self).form_valid(form)
        seller = models.Seller.objects.get(user=self.request.user)
        self.object.seller_name = seller
        self.object.save()
        return valid


class MobileUploadView(CreateView):
    form_class = forms.MobileForm
    template_name = 'seller/seller_upload.html'
    success_url = "/seller/"

    def form_valid(self, form):
        valid = super(MobileUploadView, self).form_valid(form)
        seller = models.Seller.objects.get(user=self.request.user)
        self.object.seller_name = seller
        self.object.save()
        return valid


class AddProductView(TemplateView):
    template_name = "seller/add-product.html"


class DashboardView(ListView):
    template_name = 'seller/dashboard.html'
    context_object_name = 'products'
    
    def get_queryset(self):
        model = self.kwargs['category']       
        return getattr(models, model).objects.filter(seller_name__user=self.request.user)


class Sellerservice(TemplateView):
    template_name = "seller/seller-service.html"


class ContactUsView(CreateView):
    form_class = forms.ContactUsForm
    template_name = 'seller/contactus.html'
    success_url = '/seller'


class ProductDetailView(DetailView):
    template_name = 'seller/detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        model = self.kwargs['category']
        return getattr(models, model).objects.all()    
   
class ProductUpdateView(UpdateView):
    fields = ["prod_name", "type", "price", "colour", "size", "in_stock", 'info', 'image1','image2','image3']
    template_name = 'seller/seller_upload.html'
    success_url = '/seller/SuccessfulUpdate/'

    def get_queryset(self):
        model = self.kwargs['category']
        return getattr(models, model).objects.all()  


class UpdateSuccessView(TemplateView):
    template_name = 'seller/successfulupdate.html'


class ProductDeleteView(DeleteView):
    template_name = 'seller/product_delete.html'
    success_url = '/seller/SuccessfulDelete/'

    def get_queryset(self):
        model = self.kwargs['category']
        return getattr(models, model).objects.all()  


class DeleteSuccessView(TemplateView):
    template_name = 'seller/successfulupdate.html'

    
def logoutPage(request):
    logout(request)
    return redirect("seller-home")

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("seller-home")

    form = forms.LoginForm()

    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
            if user.is_staff != False:
                user = authenticate(
                    request, username=username, password=password, is_active=True,
                )
            else:
                user = None

            if user is not None:
                login(request, user)
                return redirect("seller-home")
            else:
                messages.error(request, "Username or Password does not match...")
        except:
            messages.error(request, "User Not Found....")

    return render(request, "seller/login.html", {"form":form})
