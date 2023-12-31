from django.shortcuts import render,redirect
from items.models import Category,Item
from .forms import SignupForm
# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()
    context = {
     'items':items,
     'categories':categories,
    }
    return render(request,'index.html',context)


def contact(request):
    return render(request,'contact.html')

def signup(request):
    if request.method=="POST":
        form = SignupForm(request.POST)   
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
    else:
        print("error ")
        form = SignupForm()
        
            
        
    
    context = {
        'form':form,
    }
    return render(request,'signup.html',context)
    
    
