"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('landingpage/',views.landingpage,name='landingpage'),
    path('home/',views.home,name='home'),
    # path('Interactives/',views.Interactives,name='Interactives'),
    path('about_interactive/',views.about_interactive,name='about_interactive'),
    path('Videos/',views.Videos,name='Videos'),
    path('Resources/',views.Resources,name='Resources'),
    path('new_Login/',views.new_Login,name='new_Login'),
    path('Venue_Login/',views.Venue_Login,name='Venue_Login'),
    path('contact/',views.contact,name='contact'),
    path('terms_condition/',views.terms_condition,name='terms_condition'),
    path('accessibility/',views.accessibility,name='accessibility'),
    path('register/',views.register,name='register'),
    path('registerdata/',views.registerdata,name='registerdata'),
    path('dashboard/',views.dashboard,name='dashboard'),
    # path('',views.a,name='a'),
    path('login/',views.login,name='login'),
    path('otp/',views.otp,name='otp'),
    path('send_otp/',views.send_otp,name='send_otp'),
    path('reset/',views.reset,name='reset'),
    path('new_pass/',views.new_pass,name='new_pass'),
    # path('login_redirect/',views.login_redirect,name='login_redirect'),
    path('logout/',views.logout,name='logout'),
    path('upload/',views.upload,name='upload'),
    path('show_upload/<int:pk>/',views.show_upload,name='show_upload'),
    path('show_data/', views.show_data, name='show_data'),
    path('delete_upload/<int:pk>/',views.delete_upload,name='delete_upload'),
    # path('edit_upload/<int:pk>/',views.edit_upload,name='edit_upload'),
    path('upload_update/<int:pk>/', views.update_upload, name='update_upload'),



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
