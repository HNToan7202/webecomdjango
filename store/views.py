from django.shortcuts import render

from bson import ObjectId
from django.http import HttpResponse

from store.models import Cart
from store.models import Product
from django.views.decorators.csrf import csrf_exempt


from django.shortcuts import render, redirect  
from store.forms import ProductForm
from store.models import Product

# Create your views here.

def show(request):  
    Products = Product.objects.all()  
    return render(request,"store/store.html",{'products':Products})

def edit(request, id):  
    products = Product.objects.get(id=id)  
    return render(request,'store/edit.html', {'product':products})  

def update(request, id):  
    products = Product.objects.get(id=id)  
    form = ProductForm(request.POST, instance = products)  
    if form.is_valid():  
        form.save()  
        return redirect("/show")  
    return render(request, 'store/edit.html', {'product': products}) 

def emp(request):  
    if request.method == "POST":  
        form = ProductForm(request.POST)  
        if form.is_valid():  
            try:  
                form.save()  
                return redirect('/show')  
            except:  
                pass  
    else:  
        form = ProductForm()  
    return render(request,'store/index.html',{'form':form})  

def delete(request, id):  
    employee = Product.objects.get(id=id)  
    employee.delete()  
    return redirect("/show")

@csrf_exempt
def add_product(request):
    name=request.POST.get("name")
    post=Product(name=name)
    post.save()
    return HttpResponse("Inserted")

@csrf_exempt
def update_product(request,id):
    post=Product.objects.get(id=ObjectId(id))
    post.name=request.POST.get('name')
    post.save()
    return HttpResponse("Post Updated")

def read_product(request,id):
    post=Product.objects.get(id=ObjectId(id))
    stringval="Name : "+post.name
    return HttpResponse(stringval)

def delete_product(request,id):
    post=Product.objects.get(id=ObjectId(id))
    post.delete()
    return HttpResponse("Post Deleted")

def read_cart_all(request):
    posts=Product.objects.all()
    stringval=""
    for post in posts:
        stringval += " name : "+ post.name
    return HttpResponse(stringval)

def store(request):

	products = Product.objects.all()
	context = {'products':products}
	return render(request, 'store/store.html', context)

def cart(request):
	context = {}
	return render(request, 'store/cart.html', context)

def checkout(request):
	context = {}
	return render(request, 'store/checkout.html', context)

