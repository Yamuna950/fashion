from django.db import models

class Category(models.Model):
    name=models.CharField(max_length=20)

    @staticmethod
    def get_all_categories():
        return Category.objects.all()

    def __str__(self):
        return self.name #to show name of the category in product name 


class Product(models.Model):
    name=models.CharField(max_length=50)
    price=models.IntegerField(default=0)
    category= models.ForeignKey(Category, on_delete=models.CASCADE,default=1)
    description=models.CharField(max_length=200,default='',null=True,blank=True)
    image=models.ImageField(upload_to='uploads/products/')

    @staticmethod

    def get_all_products():
        return Product.objects.all()


    @staticmethod

    def get_all_products_by_categoryid(category_id):
        if category_id:
          return Product.objects.filter(category=category_id)

        else:
           return Product.get_all_products()


class Customer(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    email=models.EmailField()
    password=models.CharField(max_length=500)
    

    
    def register(self):
        self.save()

    @staticmethod
    def get_customer_by_email(email):
        try:
          return Customer.objects.get(email=email)
        except:
            return False
        

    def isExists(self):
        if Customer.objects.filter(email=self.email):
           return True
        return False