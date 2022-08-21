from django.contrib.auth.models import User
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=200, null=True)
    image = models.ImageField(upload_to='uploads/games/', null=True, blank=True)
    mini_1 = models.ImageField(upload_to='uploads/games/', null=True,blank=True)
    mini_2 = models.ImageField(upload_to='uploads/games/', null=True,blank=True)
    mini_3 = models.ImageField(upload_to='uploads/games/', null=True,blank=True)
    mini_4 = models.ImageField(upload_to='uploads/games/', null=True,blank=True)
    price = models.CharField(max_length=20,blank=True, null=True)
    description = models.TextField(max_length=500, null=True)

    def __str__(self):
        return (self.name)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1, blank=True, null=True)
    total = models.IntegerField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return (str(self.user) +" - "+str(self.product)+" - "+str(self.quantity)+ " - "+str(self.total))

class Contactus(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    message = models.CharField(max_length=50, blank=True, null=True)   

    def __str__(self):
        return (self.email)



order_status = (
    ('1','Pending'),
    ('2','Delivered')
)

class Orders(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    total = models.IntegerField(blank=True, null=True)
    firstname = models.CharField(max_length=100, blank=True, null=True)
    lastname = models.CharField(max_length=100, blank=True, null=True)
    email = models.CharField(max_length=100, blank=True, null=True)
    phone = models.IntegerField(blank=True, null=True)
    city = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    payment = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, choices=order_status, default='1')
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.firstname)+" "+str(self.lastname)+" - "+str(self.total)