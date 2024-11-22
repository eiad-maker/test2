from django.shortcuts import render , get_object_or_404 ,redirect
from . models import Product 
# Create your views here.

def products(request):
    pro = Product.objects.all()
    return render(request , 'products/products.html', {'product':pro})

def products_not_user(request):
    pro = Product.objects.all()
    return render(request , 'not_user/products_not_user.html', {'product':pro})

def Add_to_cart(request , product_id):
#     add = get_object_or_404(Product, pk =product_id)
    
#     if request.method == 'POST':
#         add.__dir__()
#         return redirect('products_not_user')

    return render(request , 'not_user/Add_to_cart.html' )

def Add_product(request):
    name = request.POST.get('name')
    price = request.POST.get('price')
    content = request.POST.get('content')
    image = request.POST.get('image')
    data = Product(name = name , price = price ,content = content ,image = image )
    if request.method == 'POST':
        data.save()
    return render(request , 'products/Add_product.html')

def delete_product(request , product_id):
    delete = get_object_or_404(Product , pk =product_id)
    if request.method == 'POST':
        delete.delete()
        return redirect('products')
    return render(request , 'products/delete_product.html')

def added(request):
    
    return render(request , 'not_user/added.html')

def products_user(request):
    
    return render(request , 'user/products_user.html')
