from django.shortcuts import render,HttpResponse
from django.db.models import Q

# Create your views here.
def index(request):
    #return HttpResponse('This is our Home page of ASPERFUMER')
    context={
        'variable':"Assalamallikum"
    }
    return render(request,'index.html',context)
def about(request):
    return render(request,'about.html')

    #return HttpResponse('This is our About page of ASPERFUMER')
def services(request):
    return render(request,'For You.html')

    #return HttpResponse('This is our Services page of ASPERFUMER')
def contact(request):
    return render(request,'contact.html')

    #return HttpResponse('This is our Contact page of ASPERFUMER')
def Normal_Attar(request):
    
    return render(request,'Normal Attar.html')

def Special_Attar(request):
    return render(request,'Special Attar.html')

def Premium_Attar(request):
    return render(request,'Premium Attar.html')


def Normal_Perfumes(request):
    return render(request,'Normal Perfumes.html')

def Special_Perfumes(request):
    return render(request,'Special Perfumes.html')

def Customizations(request):
    return render(request,'Customizations.html')


