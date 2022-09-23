from django.urls import path, include
from . import views
from django.contrib.auth import  views as auth_views
from .forms import LoginForm
from django.views.decorators.csrf import csrf_exempt


urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('accounts/login/', auth_views.LoginView.as_view(authentication_form=LoginForm)),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signuppage/', views.SignupView.as_view(), name='signup-page'),
    path('categorypage/<str:category>/', csrf_exempt(views.CategoryPageView.as_view()), name='category-page'),
    path('productdetail/<str:category>/<slug:slug>/', views.ProductDetilView.as_view(), name='product-detail'),
    path('cart/', views.cartPage, name='cart-page'),
    path('buynow/<str:category>/<slug:slug>/', views.buynow, name='buy-now'),
    path('addtocart/<str:category>/<slug:slug>/', views.addtocart, name='add-to-cart'),
    path('about/', views.AboutPageView.as_view(), name='about-page'),
    path('contactus/', views.ContactUsView.as_view(), name='contact-us-page'),
    path('Add-address/', views.AddAddressPageView.as_view(), name='add-address-page'),
    path('payment/<int:pk>', views.PaymentPageView.as_view(), name='payment-page'),
]
