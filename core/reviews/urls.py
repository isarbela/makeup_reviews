from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.home, name='home'),
    path('products/', views.product_list, name='product_list'),
    path('product/<int:pk>/', views.product_detail, name='product_detail'),
    path('product/<int:pk>/add_review/', views.add_review, name='add_review'),
    path('about/', views.about, name='about_us'),
    path('login/',  auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('myprofile/', views.view_profile, name='profile'),
    path('search/', views.search_results, name='search_results'),
]