from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate 



def register(request):
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password == confirm_password and email != None:
            if User.objects.filter(username=username).exists():
                return redirect('/')
            else: 
                user = User.objects.create(username=username, email=email,first_name = first_name,last_name=last_name,password=password)
                user.set_password(password)
                user.save()
                
                return redirect('/auth')
    else:
        return render(request, 'main/register.html')


def auth(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            context['error'] = 'Invalid username or password'
            return render(request,'main/auth.html',context)
        
    else:
        return render(request,'main/auth.html')
   