from django.shortcuts import render,redirect
from shop.models import Categories
from shop.models import Product
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
def categories(request):
    c=Categories.objects.all()
    context={'cat':c}

    return render(request,'categories.html',context)

def product(request,p):
    c=Categories.objects.get(id=p)
    p=Product.objects.filter(category=c)
    context={'cat':c,'product':p}
    return render(request,'product.html',context)


def details(request, p):
    pro = Product.objects.get(id=p)

    context = {'product': pro}
    return render(request, 'details.html', context)

def Register(request):
    if (request.method=="POST"):
        u = request.POST['u']
        p = request.POST['p']
        cp = request.POST['cp']
        f = request.POST['f']
        l = request.POST['l']
        e = request.POST['e']

        if (p==cp):
            u = User.objects.create_user(username=u, password=p, email=e, first_name=f, last_name=l)
            u.save()
            return redirect('shop:categories')
        else:
            return HttpResponse("password is not matching")
    return render(request,'register.html')


def User_login(request):
    if (request.method == "POST"):
        u = request.POST['u']
        p = request.POST['p']
        User = authenticate(username=u, password=p)
        if User:
            login(request, User)
            return redirect('shop:categories')
        else:
            return HttpResponse("invalid credentials")
    return render(request, 'login.html')



def User_logout(request):
    logout(request)
    return redirect('shop:register')


@login_required
def add_stock(request,k):
    p=Product.objects.get(id=k)

    if(request.method == "POST"):
        p.stock=request.POST['s']
        p.save()
        return redirect('shop:details',k)
    context={"pro":p}
    return render(request,'stock.html',context)





