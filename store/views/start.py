from django.views import  View
from django.shortcuts import render

class Start(View):
   def get(self,request):
      return render(request,'home.html')