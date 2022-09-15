from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.index),
    path('search',views.search),
    path('search-action',views.search_action,name="search_action"),
    path('signup',views.signup,name="sigup"),
    path('signup-action',views.signup_action,name="signup_action"),
    path('sigin',views.sigin,name="sigin"),
    path('sigin-action',views.sigin_action,name="sigin_action"),

    
]
from django.conf import settings
from django.conf.urls.static import static
urls += static(setting.MEDIA_URL,document_root = setting.MEDIA_ROOT)
