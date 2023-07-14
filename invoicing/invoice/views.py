from django.shortcuts import render
from django.views import View
from .serializer import *
from .data import *
from django.http import JsonResponse
import uuid
import json
# Create your views here.

class AllInvoices(View):
    def get(self,request):
        serializer = InvoicesSerializer(invoicesData,many=True).data
        return JsonResponse(serializer,safe=False)


    def post(self,request):
        data = json.loads(request.body)
        data["invoice_id"]=len(invoicesData)+1
        print(data)
        serializer = InvoicesSerializer(data=data)
        if serializer.is_valid():
            invoicesData.append(serializer.data)
            return JsonResponse(serializer.data,safe=False)
        return JsonResponse(serializer.errors,safe=False)

class SpecificInvoices(View):
    def get(self,request,id):
        for val in invoicesData:
           if val["invoice_id"] == id:
                serializer = InvoicesSerializer(val).data  
                return JsonResponse(serializer,safe=False) 
        return JsonResponse({"message:""No Invoice found"})          
  

class AddItems(View):
     def post(self,request,id):
        data =json.loads(request.body)
        serializer=Itemserializers(data=data)
        if serializer.is_valid():
            for val in invoicesData:
                if val["invoice_id"] ==id:
                    val["items"].append(serializer.data)
                    return JsonResponse(serializer.data,safe=False) 
                return JsonResponse({"message:""No Invoice found"}) 
            return jsonResponse(serializer.errors,safe=False)

class SignupView(View):
     def post(self,request):
        data = json.loads(request.body)
        data["user_id"]=len(userData)+1
        serializer=Userserializer(data=data)
        if serializer.is_valid():
            userData.append(serializer.data)
            return JsonResponse(serializer.data,safe=False)
        return JsonResponse(serializer.errors,safe=False)
class SigninView(View):
    def post(self,request):
        data = json.loads(request.body)
        for val in userData:
            if val["email"]==data["email"]and val["password"]==data["password"]:
                token=str(uuid.uuid4())
                return JsonResponse({"messages":"login sucess","token":token,"state":True})
        return JsonResponse({"messages":"Not Valid Credentials","state":False})
    
                        







