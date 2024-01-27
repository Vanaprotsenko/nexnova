from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from order.models import Bucket, ProductBucket, Product
from django.http import JsonResponse


def product_page(request, product_id):
    context = {}
    user = request.user

    bucket = Bucket.objects.filter(user_id=user).first()

    product = get_object_or_404(Product, pk=product_id)
    bject_count = ProductBucket.objects.filter(bucket=bucket).count()
    context = {
        'product': product,
        'count': bject_count
    }
    
    return render(request,'product/product.html', context)
    

def automatic(request):
    context = {}
    user = request.user
    bucket = Bucket.objects.filter(user_id=user).first()
    object_count = ProductBucket.objects.filter(bucket=bucket).count()

    data = {'key': object_count} 
   
    json_data = JsonResponse(data) 
    context = {
        'json_data': json_data
    }
    return render(request,'product/catalog.html',context)
    

@login_required
def add_to_bucket(request,product_id):       

    user = request.user
    
    bucket,  create = Bucket.objects.get_or_create(user=user)
    product = Product.objects.get(pk=product_id)
    ProductinBucket = ProductBucket.objects.create(count=1,product=product, bucket=bucket)
    
    return redirect(f'/products/{product_id}/')
    

def catalog_page(request):
    context = {}
    user = request.user

    bucket = Bucket.objects.filter(user_id=user).first()
    
    bject_count = ProductBucket.objects.filter(bucket=bucket).count()   
    
    products = Product.objects.all()
    
    productbucket = ProductBucket.objects.all()
    context = {
        'products': products,
        'productbucket': productbucket,
        'count': bject_count,
        'user': user
        
    }
    return render(request, 'product/catalog.html', context)


def product_search(request):
    context = {}
    query = request.GET.get('query', '')

    if query:
        products = Product.objects.filter(category__name__iexact=query)
        product_name = Product.objects.filter(name__iexact=query)

        context = {
            'products': products,
            'product_name': product_name,
        }

    return render(request, 'product/category.html', context)






    
