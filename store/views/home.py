from django.shortcuts import render
from django.shortcuts import render,redirect
from store.models import Product,Category,Customer
from django.views import View

#print(make_password('1234'))
# Create your views here.


class Index(View):
    def post(self,request):
       product=request.POST.get('product')
       cart= request.session.get('cart')
       if cart:
           quantity=cart.get(product)
           if quantity:
              cart[product]=quantity+1
           else:
              cart[product]=1
            
       else:
           cart={}
           cart[product]=1
       request.session['cart']=cart
       print('cart',request.session['cart'])
       return redirect('homepage')
    


    def get(self,request):
         products=None
         #request.session.get('cart').clear()
         products= Product.get_all_products()
         categories=Category.get_all_categories()
         # return render(request, 'orders/order.html') 
         categoryID=request.GET.get('category')
         if categoryID:
           products=Product.get_all_products_by_categoryid(categoryID)
         else:
          products=Product.get_all_products()
         data={}
         data['products']=products
         data['categories']=categories
         print('you are:',request.session.get('email'))
         return render(request, 'index.html',data)




  


    

    


