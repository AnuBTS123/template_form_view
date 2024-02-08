from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from app.forms import *
from django.http import HttpResponse
# Create your views here.

class TemplateHtml(TemplateView):
    template_name='TemplateHtml.html'

    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['name']='Anuhya'
        ECDO['age']=22
        return ECDO
    
class InsertBookByTV(TemplateView):
    template_name='InsertBookByTV.html'

    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        ECDO['BFO']=BookForm
        return ECDO
    
    def post(self,request):
            BFDO=BookForm(request.POST)
            if BFDO.is_valid():
                 BFDO.save()
                 return HttpResponse('InsertBookByTV is done')
            

class InsertBookByFV(FormView):
     template_name='InsertBookByFV.html'
     form_class=BookForm
     def form_valid(self,form):
          form.save()
          return HttpResponse('InsertBookByFV is done')