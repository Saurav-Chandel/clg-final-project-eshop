from django.contrib import admin
from django.urls import path
from .views.home import Index ,store
from .views.carousel import carousel
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import *
from .views.checkout import CheckOut
from .views.orders import OrderView
from .middlewares.auth import  auth_middleware
from .views.start import Start


urlpatterns = [
    path('', Index.as_view(), name='homepage'),
    path('home',Start.as_view(),name='home'),
    path('store', store , name='store'),
    path('carousel', carousel , name='carousel'),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),
    path('checkout-session/<int:id>/', create_checkout_session, name='api_checkout_session'),

    path('success/', PaymentSuccessView.as_view(), name='success'),
    path('failed/', PaymentFailedView.as_view(), name='failed'),
]
