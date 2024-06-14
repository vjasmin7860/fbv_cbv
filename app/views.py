from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *

# Create your views here.

#creating a string by using fbv
def string_by_fbv(request):
    return HttpResponse('here function based view is created successfully')


# here creating a string by using cbv

class StringByCbv(View):
    def get(self,request):
        return HttpResponse('class based view is created successfully')
    


# creating html pages by using fbv

def html_by_fbv(request):
    return render(request,'html_by_fbv.html')



#here we are creating html pages by using cbv


class HtmlByCbv(View):
    def get(self,request):
        return render(request,'HtmlByCbv.html')
    



#here we are creating (inserting) forms by using models.


def insert_by_fbv(request):
    d={'ESFO':SchoolForm()}
    if  request.method=='POST':
        ESFO=SchoolForm(request.POST)
        if ESFO.is_valid():
            ESFO.save()
            return HttpResponse('school form is created successfully')
        else:
            return HttpResponse('invalid data')
    return render(request,'insert_by_fbv.html',d)


#here we are creating (inserting) forms by using cbv

class Insert_By_Cbv(View):
    def get(self,request):
        d={'ESFO':SchoolForm()}
        return render(request,'Insert_By_Cbv.html',d)
    

    def post(self,request):
        ESFO=SchoolForm(request.POST)
        if ESFO.is_valid():
            ESFO.save()
            return HttpResponse('school form is created successfully')
        else:
            return HttpResponse('invalid data')



# creating template view

class Html_By_Tv(TemplateView):
    template_name='Html_By_Tv.html'