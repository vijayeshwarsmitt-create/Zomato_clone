from django.shortcuts import render, get_object_or_404
from .models import Restaurant, Menu

def home(request):
    restaurants = Restaurant.objects.all()
    return render(request, 'home.html', {'restaurants': restaurants})


def restaurant_detail(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    menu = Menu.objects.filter(restaurant=restaurant)
    return render(request, 'restaurant.html', {
        'restaurant': restaurant,
        'menu': menu})

def add_to_cart(request, id):
    cart = request.session.get('cart', {})
    cart[str(id)] = cart.get(str(id), 0) + 1
    request.session['cart'] = cart
