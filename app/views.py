import random
from django.db import models

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse

from .models import Mobile, Company, Booking
from .forms import MobileForm, HotelForm

from django.views.generic.edit import CreateView, UpdateView

# :)


def index(request):
    number = random.randint(10, 100)
    content = f"""
        <div style="margin:1em auto; padding:1em; background: #e74c3c; box-shadow: 0px 8px 16px rgba(0,0,0,0.2); border-radius: 16px; width: 300px;">
        <h1 style="color: #c0392b;">Hey There! Welcome</h1>
        <p style="color: #efefef;"> Refresh page, and you will get a random number each time</p>
        <p style="font-size: 4em; text-align:center; color: #fc7365;">{number}</p>
        </div>
    """
    return HttpResponse(content)

# ;)


def homepage(request):
    return render(request, 'base.html')


def say_hello(request):
    return HttpResponse('<h1>Hello World</h1>')

# :(


def logout(request):
    return HttpResponse("<h1>No!!!!!!! Please stay, don't leave</h1>")


def echo(request, day, month, year):
    return HttpResponse(f"<h1>Today is {day}-{month}-{year}</h1>")


PRODUCTS = {
    'laptops': ['HP', 'DELL', 'Lenovo', 'Acer', 'Mac', "IBM", "COMPAQ"],
    'mobiles': ['Samsung', 'iPhone', 'Vivo', 'ifinix', 'OPPO'],
    'bikes': ['Honda CD70', 'Yahmaha YBRG 125', 'Haya Bussa', 'Ducati', 'Harley Davidson'],
}


def list_products(request, name):
    # context
    context = {
        "name": '',
        "product_list": [],
        "result_count": 0
    }

    context['category_name'] = name
    if name in PRODUCTS:
        context['product_list'] = PRODUCTS[name]
        context['result_count'] = len(PRODUCTS[name])

    return render(request, 'base.html', context)


# PROFILE = {
#   Management = [
#       {id: 1, slug:john-doe1 name:John Doe, age:450, email:john@gmail.com, designation: HR Manager } x 3-4
#       ],
#   Developers = [
#       {id: 2, slug=john-doe-2, name:John Doe 2, age:450, email:john@gmail.com, designation: Laravel Dev } x 3-4
#       ],
#   Interns = [
#       {id: 2, slug=john-doe-2, name:John Doe 2, age:450, email:john@gmail.com, program: Laravel Dev } x 3-4
#       ]
# }

# 2 types of routes
# heirarchy - id, slug, age
# Search by ID
# Search by Slug
# Search by lt and eq age

PROFILES = {
    "Management": [
        {
            "id": 1,
            "slug": "john-doe",
            "name": "John Doe",
            "age": 27,
            "email": "john@gmail.com",
            "designation": "CEO"
        },
        {
            "id": 2,
            "slug": "kai-doe",
            "name": "Kai Doe",
            "age": 26,
            "email": "kai@gmail.com",
            "designation": "CTO"
        }
    ],
    "Developers": [
        {
            "id": 11,
            "slug": "john-brass",
            "name": "John Brass",
            "age": 24,
            "email": "johnbrass@gmail.com",
            "designation": "Senior Developer"
        },
        {
            "id": 12,
            "slug": "sohaib-tanveer",
            "name": "Sohaib Tanveer",
            "age": 24,
            "email": "sohaib@gmail.com",
            "designation": "Junior Developer"
        },
    ],
    "Interns": [
        {
            "id": 31,
            "slug": "nauman-ahmad",
            "name": "Nauman Ahmad",
            "age": 24,
            "email": "nomismart@gmail.com",
            "designation": "Data Scientist"
        },
        {
            "id": 32,
            "slug": "hasaan-haider",
            "name": "Hasaan Haider",
            "age": 26,
            "email": "hhaider@gmail.com",
            "designation": "Data Scientist"
        },
    ]
}


def search_by_heirarchy_and_id(request, heirarchy, id):
    context = {
        "heirarchy": heirarchy,
        "keyword": id,
        "received_by": 'search_by_heirarchy_and_id',
        "member": None
    }

    members = PROFILES[heirarchy]
    for member in members:
        if member['id'] == id:
            context['member'] = member

    return render(request, 'base.html', context)


def search_by_heirarchy_and_slug(request, heirarchy, slug):
    context = {
        "heirarchy": heirarchy,
        "keyword": id,
        "received_by": 'search_by_heirarchy_and_id',
        "member": None
    }

    members = PROFILES[heirarchy]
    for member in members:
        if member['slug'] == slug:
            context['member'] = member

    return render(request, 'base.html', context)


def search_by_heirarchy_and_age(request, heirarchy, age):
    context = {
        "heirarchy": heirarchy,
        "keyword": age,
        "received_by": 'search_by_heirarchy_and_id',
        "member": None,
        "members": []
    }

    members = PROFILES[heirarchy]
    for member in members:
        if member['age'] <= age:
            context['members'].append(member)

    return render(request, 'base.html', context)


# FORM
def list_products(request):
    return render(request, 'app/products.html')


def add_product(request):
    product = {
        "name": '',
        "price": 0,
        "quantity": 0,
        "description": '',
        "category": ''
    }

    # GET REQUEST
    if request.method == 'GET':
        # Query Parameters (Query Params)
        product_name = request.GET.get('product-name', 'NO PRODUCT NAME')
        product_price = request.GET.get('product-price', -1)
        product_quantity = request.GET.get('product-quantity', -1)
        product_description = request.GET.get(
            'product-description', 'No Description Provided')
        product_category = request.GET.get(
            'product-category', 'No Category Provided')

        product['name'] = product_name
        product['price'] = product_price
        product['quantity'] = product_quantity
        product['description'] = product_description
        product['category'] = product_category

        # print("Don't save here, never!", request.GET, product)

    # POST
    if request.method == 'POST':
        product_name = request.POST.get('product-name', 'NO PRODUCT NAME')
        product_price = request.POST.get('product-price', -1)
        product_quantity = request.POST.get('product-quantity', -1)
        product_description = request.POST.get(
            'product-description', 'No Description Provided')
        product_category = request.POST.get(
            'product-category', 'No Category Provided')

        product['name'] = product_name
        product['price'] = product_price
        product['quantity'] = product_quantity
        product['description'] = product_description
        product['category'] = product_category

        print("POST DATA:::", product)

    return render(request, 'app/product_form.html')


def form_receiver(request):
    print("Form data received")
    return render(request, 'base.html')


# ----------------------------
#
#   M O B I L E CRUD Operations
#
# ----------------------------
def list_mobiles(request):
    context = {
        'list': []
    }

    mobiles = Mobile.objects.all()
    context['usman'] = mobiles
    context['count'] = mobiles.count()

    return render(request, 'app/mobile/list.html', context)


def create_mobile_old(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        company = request.POST.get('company', '')
        price = request.POST.get('price', 0)
        color = request.POST.get('color', '')
        is_new = 'is_new' in request.POST
        features = request.POST.get('feature', '')

        # Method 1
        mobile = Mobile()
        mobile.name = name
        mobile.company = company
        mobile.price = price
        mobile.color = color
        mobile.is_new = is_new
        mobile.features = features

        mobile.save()

        return redirect('mobile-list')

    return render(request, 'app/mobile/form.html')


def retrieve_mobile(request, id):
    # filter
    # get_or_404
    # error handling
    mobile= get_object_or_404(Mobile, id=id)
    context = {
        'mobile': mobile
    }
    return render(request, 'app/mobile/detail.html', context)


def update_mobile(request, id):
    mobile = Mobile.objects.get(id=id)
    context = {
        'mobile': mobile
    }

    if request.method == "POST":
        name = request.POST.get('name', '')
        company = request.POST.get('company', '')
        price = request.POST.get('price', 0)
        color = request.POST.get('color', '')
        is_new = 'is_new' in request.POST
        features = request.POST.get('feature', '')

        mobile.name = name
        mobile.company = company
        mobile.price = price
        mobile.color = color
        mobile.is_new = is_new
        mobile.features = features

        mobile.save()

        return redirect('mobile-list')

    return render(request, 'app/mobile/form.html', context)


def delete_mobile(request, id):
    mobile = get_object_or_404(Mobile, id=id)
    mobile.delete()

    return redirect('mobile-list')


def create_mobile(request):
    context = {
        "form": MobileForm()
    }
    if request.method == "POST":
        form = MobileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('mobile-list')
        else:
            context['form'] = form
            context['errors'] = form.errors

    return render(request, 'app/mobile/form.html', context)

# CBV = Class Based View


class MobileCreate(CreateView):
    model = Mobile
    form_class = MobileForm
    template_name = "app/mobile/form.html"



#########################
#
#   HOTEL Bookings
#
########################


def list_bookings(request):
    context = {
        'list': []
    }

    booking = Booking.objects.all()
    context['usman'] = booking
    context['count'] = booking.count()

    return render(request, 'app/hotel/list.html', context)





def create_booking(request):
    context={
    'form': HotelForm()
    }

    if request.method== 'POST':
        form=HotelForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('booking-list')

        else:
            context['form']=form
            context['errors']= form.errors

    return render(request, 'app/hotel/form.html', context)



def retrieve_booking(request, id):

    booking= get_object_or_404(Booking, id=id)
    context = {
        'booking': booking
    }
    return render(request, 'app/hotel/detail.html', context)


def update_booking(request, id):
    obj = get_object_or_404(Booking, id=id)
    form=HotelForm(request.POST, instance=obj)
    if request.method== 'POST':
        
        if form.is_valid():
            form.save()
            return redirect('booking-list')


    return render(request, 'app/hotel/form.html', {'form':form})



def delete_booking(request, id):
    booking = get_object_or_404(Booking, id=id)
    booking.delete()

    return redirect('booking-list')



