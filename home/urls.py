from django.urls import path
from . import views
from marketing.views import email_list_signup


urlpatterns = [
    path('', views.index, name='home'),
    path('email_list_signup', email_list_signup, name='email_list_signup'),
]
