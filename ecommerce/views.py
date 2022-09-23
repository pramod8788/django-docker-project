from re import T
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse
from django.urls.base import reverse_lazy
from django.shortcuts import render, redirect
from . import models
from . import forms
import random


# Create your views here.
User = get_user_model()

class HomeView(View):

    def contexData(self):
        try:
            carousel_item = models.Carousel.objects.all()
            homedecor_prod = models.HomeDecor.objects.all().order_by('-pk')[:4]
            fashion_prod = models.Fashion.objects.all().order_by('-pk')[:4]
            electronic_prod = models.Electronic.objects.all().order_by('-pk')[:6]
            mobile_prod = models.Mobile.objects.all().order_by('-pk')

            combined_list = list(electronic_prod) + list(fashion_prod) + list(homedecor_prod) + list(mobile_prod)
            result_list = []
            for i in range(20):
                val = random.choice(combined_list)
                if val in result_list:
                    continue
                else:
                    result_list.append(val)

            context = {
                "carousel":carousel_item,
                "electronic_prod":electronic_prod,
                "fashion_prod":fashion_prod,
                "homedecor_prod":homedecor_prod,
                "result_list":result_list,
            }

            return context
        except:
            return messages.error(self.request, "Try again later")

    def get(self, request):
        return render(request, 'ecommerce/home.html', self.contexData())


class SignupView(CreateView):
    template_name = 'ecommerce/signup.html'
    model = User
    form_class = forms.ModifiedUserForm
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        valid = super(SignupView, self).form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        new_user = authenticate(username=username, password=password)
        login(self.request, new_user)
        return valid


class ProductDetilView(DetailView):
    template_name = 'ecommerce/product-detail.html'
    context_object_name = 'product'

    def get_queryset(self):
        model = self.kwargs['category']
        return getattr(models, model).objects.all()      


class CategoryPageView(TemplateView):
    template_name = 'ecommerce/category-products.html'
    # context_object_name = 'category_prod'

    def get_context_data(self, **kwargs):
        context_value = super().get_context_data(**kwargs)
        model = self.kwargs['category']

        all_products = getattr(models, model).objects.all().order_by('-pk')

        type_filter = self.request.GET.get("type_filter")
        if type_filter == "price_low":
            all_products = getattr(models, model).objects.all().order_by('price')
        elif type_filter == "price_high":
            all_products = getattr(models, model).objects.all().order_by('-price')
        elif type_filter:
            all_products = getattr(models, model).objects.filter(type=type_filter)

        context_value["category_prod"] = all_products
        
        choice_type = getattr(models, model).type_choice
        list_choice = []
        for item in choice_type:
            list_choice.append(item[0])
        context_value["type_filter"] = list_choice

        return context_value

    # def get_queryset(self):
    #     model = self.kwargs['category']
    #     return getattr(models, model).objects.all().order_by('-pk')


class AboutPageView(TemplateView):
    template_name = 'ecommerce/about.html'


class ContactUsView(CreateView):
    form_class = forms.ContactUsForm
    template_name = 'ecommerce/contactus.html'
    success_url = '/'


class AddAddressPageView(CreateView):
    template_name = 'ecommerce/add-address.html'
    form_class = forms.AddressForm
    success_url = '/Add-address'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data["old_address"] = models.Address.objects.filter(user=self.request.user)
        return data

    def form_valid(self, form):
        valid_data =  super(AddAddressPageView, self).form_valid(form)
        self.object.user = self.request.user
        self.object.save()
        return valid_data


class PaymentPageView(TemplateView):
    template_name = "ecommerce/payment-page.html"

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        
        address = models.Address.objects.get(id=self.kwargs['pk'])
        context_data["address"] = address
        
        cart_item = models.Cart.objects.filter(user=self.request.user)
        items_list = []
        price_list = []
        for item in cart_item:
            val = getattr(models, item.category).objects.get(slug=item.product)
            a = val.price * item.quantity
            price_list.append(a)
            items_list.append([val, item])

        total_amount = sum(price_list)
        context_data["item_list"] = items_list
        context_data["price_list"] = price_list
        context_data["total_amount"] = total_amount

        return context_data


@login_required(login_url="login")
def cartPage(request):
    if request.method == "POST":
        quantity = request.POST.get('quantity')
        if quantity == 'all':
            item = request.POST.get('cart_item')
            models.Cart.objects.get(pk=item).delete()

        elif quantity == 'plus':
            item = request.POST.get('cart_item')
            obj = models.Cart.objects.get(pk=item)
            if obj.quantity < 10:
                obj.quantity += 1
                obj.save()

        elif quantity == 'minus':
            item = request.POST.get('cart_item')
            obj = models.Cart.objects.get(pk=item)
            if obj.quantity > 1:
                obj.quantity -= 1
                obj.save()
            else:
                obj.delete()

    cart_item = models.Cart.objects.filter(user=request.user)
    items_list = []
    price_list = []
    for item in cart_item:
        val = getattr(models, item.category).objects.get(slug=item.product)
        a = val.price * item.quantity
        price_list.append(a)
        items_list.append([val, item])

    total_amount = sum(price_list)

    context = {
        "item_list" : items_list,
        "price_list" : price_list,
        "total_amount" : total_amount,
    }
    return render(request, "ecommerce/cart.html", context)


@login_required(login_url="login")
def buynow(request, category, slug):
    cart_item = models.Cart.objects.filter(user=request.user)

    val = 0
    for item in cart_item:
        if item.category == category and item.product == slug:
            item.quantity += 1
            item.save()
            val += 1
            break
        else:
            continue

    if val == 0:
        models.Cart.objects.create(user=request.user, product=slug, category=category)

    return redirect('cart-page')


@login_required(login_url="login")
def addtocart(request, category, slug):
    cart_item = models.Cart.objects.filter(user=request.user)

    val = 0
    for item in cart_item:
        if item.category == category and item.product == slug:
            item.quantity += 1
            item.save()
            val += 1
            break
        else:
            continue

    if val == 0:
        models.Cart.objects.create(user=request.user, product=slug, category=category)

    messages.error(request, "Item added to cart")
    val = reverse('product-detail', args=[category, slug])
    return redirect(val)