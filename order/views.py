from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from order.models import Bucket, ProductBucket,  Product
import requests


def create_order(request):
    context = {}
    
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'order/create_order.html', context)


@login_required
def send_message_to_telegram(request):
    
    context = {}
    user = request.user
    product_buckets = []
    total_price = 0  
    all_data_str = []
    data_all = []

    bucket = Bucket.objects.filter(user_id=user).first()
    
    if bucket:
        product_buckets = ProductBucket.objects.filter(bucket=bucket)
        data_all = []
        total_price = sum(product_bucket.product.price * product_bucket.count for product_bucket in product_buckets)    
        for named in product_buckets:
            total_data = named.product.name + "\n" + str(named.product.price) + "\n" + str(named.count)
            data_all.append(total_data)
            all_data_str = "\n".join(data_all)                  
    else:
        product_buckets = []
        total_price = 0  
        all_data_str = []
        data_all = []

    context = {
        'product_buckets': product_buckets,
        'total_price': total_price,    
        'all_data_str': all_data_str,
        'data_all': data_all,
        'user': user
    }
    
    if request.method == 'POST':
        
        email = request.POST.get('email', '')
        full_name = request.POST.get('full_name', '')
        phone_number = request.POST.get('phone_number', '')
        
        full_info = "Email user" + " : " + email + "\n" + "Name" + " : " + full_name + "\n" + " Phone number" + " : " + phone_number +"\n" + all_data_str
        
        bot_token = '6610207148:AAGIhjLC9Jx0w-j6JzT8u__mxlnjvfOLw2k'
        chat_id = '5334960289'

        telegram_api_url = f'https://api.telegram.org/bot{bot_token}/sendMessage'
        data = {
            'chat_id': chat_id,
            'text': full_info,
        }
        
        response = requests.post(telegram_api_url, data=data)

        if response.status_code == 200:
            context = {'message': 'Заказ принят и отправлен в Telegram'}
            
        else:
            context = {'message': 'Что-то пошло не так при отправке заказа в Telegram'}

    return render(request, 'order/cart.html',context)