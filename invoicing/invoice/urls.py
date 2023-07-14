from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns=[
   
    path("invoices",csrf_exempt(AllInvoices.as_view()),name="invoices"),
    path("invoices/new",csrf_exempt(AllInvoices.as_view()),name="newinvoices"),
    path("invoices/<int:id>",SpecificInvoices.as_view(),name="SpecificInvoices"),
    path("invoices/<int:id>/items",csrf_exempt(AddItems.as_view()),name="AddItems"),
    path("signup",csrf_exempt(SignupView.as_view()),name="SignupView"),
    path("signin",csrf_exempt(SigninView.as_view()),name="SigninView")
  
    ]