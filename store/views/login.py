from django.views import View
from django.shortcuts import render,redirect
from django.contrib.auth.hashers import check_password
from store.models import Product,Category,Customer
from django.views import View


class Login(View):
    def get(self, request):
        return render(request,'login.html')
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        customer=Customer.get_customer_by_email(email)
        error_message=None
        if customer:
            flag=check_password(password,customer.password)
            if flag:
                request.session['customer_id']=customer.id
                request.session['email']=customer.email
                return redirect('homepage')
            else:
                error_message="email or password invalid"
        else:
            error_message="email or password invalid"
        print(customer)
        print(email,password)
        return render(request,'login.html',{'error':error_message})


