from django.shortcuts import redirect, render
from django.contrib.auth import login, logout
from .models import Orders, Product, Cart, Contactus
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    products = Product.objects.all()
    context = { 'products' : products }
    return render(request, "index.html", context)

def gameDetailView(request, pk):
    # view clicked game
    game = Product.objects.get(id=pk)
    context = { 'game' : game }
    return render(request, "game-detail-view.html", context)

def add_to_cart(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            user = request.user
            quantity = int(request.POST.get('quantity'))
            game = Product.objects.get(id=request.POST.get('game-id'))

            # calculate total for specific game as per quantity
            price = int(game.price)
            total = int(price)*int(quantity)

        # get a game that is (active), users, product=game 
        if Cart.objects.filter(user=user ,product=game, active=True).exists():
            game_item=Cart.objects.get(user=user, product=game)
            # increase total and quantity
            if game_item != None:
                game_item.total += total
                game_item.quantity += quantity
                game_item.save()
        else:
            # if not exists then create one
            cart = Cart.objects.create(user=user, product=game, quantity=quantity, total=total, active=True)
            cart.save()
            return redirect('cart')
    return redirect('home')

def remove_from_cart(request):
    if request.method == "POST":
        # get id cart-item id from hidden from and remove
        cart_id_item = request.POST.get('cart-id')
        cart_item = Cart.objects.filter(id=cart_id_item).exists()
        if cart_item:
            Cart.objects.filter(id=cart_id_item).delete()
            return redirect('cart')    
    return redirect('cart')

def go_to_cart(request):
    if request.user.is_authenticated:
        user = request.user
        # if there is games in users cart
        if Cart.objects.filter(user=user).exists():
            # take all the (active) games that belongs to user 
            cart_items = Cart.objects.filter(user=user, active=True)

            # calculate total for all games in cart for every game that user put in cart
            cart_total = 0
            for i in cart_items.values('total'):
                cart_total += i['total']
  
            context = {'items':cart_items, 'total':cart_total}
            return render(request, 'cart.html', context) 
    return redirect('home')
    
def register(request):
    # create new user store in DB
    if request.method == "POST":
        if User.objects.filter(username=request.POST.get("username"),  password=request.POST.get("password")).exists():
            return redirect('error')
        else:
            user = User.objects.create(username=request.POST.get("username"), password=request.POST.get("password"))
            user.save()
            return redirect('home')
    else:
        if request.user.is_authenticated == False:
            return render(request, 'register.html')
        else:
            return redirect('home')

def login_user(request):
    # login user if data is valid 
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")  
        user = User.objects.filter(username=username, password=password).exists()
        if user:
            user_logger = User.objects.get(username=username, password=password)
            login(request, user_logger)
            return redirect('home')
        else:
            return render(request, 'login.html')
    else:
        if request.user.is_authenticated == False:
            return render(request, 'login.html')
        else:
            return redirect('home')

def logout_user(request):
    logout(request)
    return redirect('home')

def about_us(request):
    return render(request, 'about-us.html')

def contact_us(request):
    # take from data and store in DB
    if request.method == "POST":
        name = request.POST.get('person-name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        msg = request.POST.get('msg')
        
        data = Contactus.objects.create(name=name, email=email, phone=phone, message=msg)
        data.save()
        return render(request, 'contact-us.html')
    return render(request, 'contact-us.html')

def makeOrder(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            user = request.user

            fn = request.POST.get('first-name')
            ln = request.POST.get('last-name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            city = request.POST.get('city')
            state = request.POST.get('state')
            address = request.POST.get('address')
            pm = request.POST.get('pm')
            #get cart total from hidden field
            total = request.POST.get('total')

            #get games that is (active and user belongs)
            user_cart_items = Cart.objects.filter(user=user, active=True)
            
            for i in user_cart_items:
                order = Orders.objects.create(user=user, cart=i, total=i.total,  firstname=fn, lastname=ln, email=email, phone=phone, city=city, state=state,  address=address, payment=pm)
                i.active = False
                i.save()
            # redirect to my orders page    
            return redirect('my-order')
    else:
        return redirect('home')

def checkout(request):
    #pass the total to store in order DB
    if request.method == "POST":
        total = request.POST.get('total')
        context = {'total':total}
        return render(request, 'checkout.html', context)
    else:
        return redirect('home')


def myOrders(request):
    if request.user.is_authenticated:
        user = request.user

        # get deavtive carts means purchesd games
        user_cart = Cart.objects.filter(user=user, active=False)
        user_orders = Orders.objects.filter(user=user)
        context = {'items':user_orders}
    return render(request, 'myorders.html', context)


def error(request):
    context = {'user_exist':'User already exist try using different username'}
    return render(request, 'error.html', context)