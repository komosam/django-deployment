from django.shortcuts import render
from bikes.forms import registration_form
# Create your views here.

def index(request):
    return render(request,'bikes_temp/index.html')

#def others(request):
    #form = registration_form()

    #if request.method == 'POST':
        #if form.is_valid():
        #form = registration_form(request.POST)
        #form.save(commit=True)
        #return index(request)
    #else: print ('form invalid')
    #return render(request,'bikes_temp/others.html',{'form':form })

def base(request):
    return render(request,'bikes_temp/base.html')

def other(request):
    return render(request,'bikes_temp/other.html')

def brand(request):
    return render(request,'bikes_temp/brand.html')
