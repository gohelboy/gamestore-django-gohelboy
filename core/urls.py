from django.urls import path
from . import views

urlpatterns = [
    path('',views.home ,name='home'),
    path('register/', views.register, name='register'),
    path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('about-us/', views.about_us, name='about-us'),
    path('contact-us/', views.contact_us, name='contact-us'),
    path('add-to-cart/', views.add_to_cart),
    path('remove-from-cart/', views.remove_from_cart),
    path('cart/', views.go_to_cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('order/', views.makeOrder, name='order'),
    path('my-order/', views.myOrders, name='my-order'),
    path('error/', views.error, name='error'),
    path('<pk>/',views.gameDetailView),
]

