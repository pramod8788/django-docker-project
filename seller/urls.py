from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm
from django.contrib.auth.decorators import login_required

urlpatterns = [
    path("", views.Home.as_view(),name='seller-home'),
    path("LoginPage/", views.loginPage, name="seller-login"),
    path("LogoutPage/", views.logoutPage, name="seller-logout"),
    path('SellerSignup/', views.SellerSignupView.as_view(),name='seller-signup'),

    path("AddProducts/", views.AddProductView.as_view(),name='upload-newproduct'),
    path("ElectronicsItemUpload/", views.ElectronicUploadView.as_view(),name='eupload-product'),
    path("FashionItemUpload/", views.FashionUploadView.as_view(),name='upload-product'),
    path("HomeDecorItemUpload/", views.HomeDecoreUploadView.as_view(),name='hdupload-product'),
    path("MobileItemUpload/", views.MobileUploadView.as_view(),name='mupload-product'),

    path("Dashboard/<str:category>/", login_required(views.DashboardView.as_view(),login_url='seller-login'), name='dashboard'),
    path("ProductDetail/<str:category>/<slug:slug>/", login_required(views.ProductDetailView.as_view(),login_url='seller-login'), name='detail'),
    path('Edit/<str:category>/<slug:slug>/', views.ProductUpdateView.as_view(),name='edit'),
    path("SuccessfulUpdate/", views.UpdateSuccessView.as_view(), name="success"),
    path('SellerService/', views.Sellerservice.as_view(),name='seller-service'),
    path('contactus/', views.ContactUsView.as_view(), name='seller-contact-us-page'),
    path('Delete/<str:category>/<slug:slug>/', views.ProductDeleteView.as_view(), name='delete'),
    path("SuccessfulDelete/", views.DeleteSuccessView.as_view(), name="success"),
]