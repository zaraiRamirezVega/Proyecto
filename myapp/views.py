import csv
import random
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm, LoginForm

CSV_FILE_PATH = 'users.csv'
PRODUCTS_FILE_PATH = 'products.csv'

def home(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            return handle_login(request)
        elif 'register' in request.POST:
            return handle_register(request)
    else:
        login_form = LoginForm()
        register_form = RegisterForm()
    
    return render(request, 'home.html', {
        'login_form': login_form,
        'register_form': register_form
    })

def handle_login(request):
    form = LoginForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        with open(CSV_FILE_PATH, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == username and row[1] == password:
                    # Redirect to products view with the username as a query parameter
                    return redirect(f'/products/?user={username}')
            return HttpResponse("Error: Invalid username or password")
    return redirect('home')

def handle_register(request):
    form = RegisterForm(request.POST)
    if form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        age = form.cleaned_data['age']
        gender = form.cleaned_data['gender']
        with open(CSV_FILE_PATH, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([username, password, age, gender])
        return redirect('home')
    return redirect('home')

def products(request):
    username = request.GET.get('user')

    if not username:
        return redirect('home')

    # Encuentra el género del usuario
    gender = None
    try:
        with open(CSV_FILE_PATH, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                if row[0] == username:
                    gender = row[3]  # Asumiendo que el género está en la cuarta columna
                    break
    except FileNotFoundError:
        return HttpResponse("Users file not found")

    products = {
        'on_offer': [],
        'popular': [],
        'recommended': []
    }
    
    try:
        with open(PRODUCTS_FILE_PATH, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            all_products = list(reader)
            
            # Sort products by price and get the 7 cheapest for the offers
            all_products_sorted_by_price = sorted(all_products, key=lambda row: float(row['precio']))
            products['on_offer'] = all_products_sorted_by_price[:7]  # First 7 cheapest as offers
            
            # Get top 10 popular products (sorted by likes)
            products['popular'] = sorted(all_products, key=lambda row: int(row['me_gusta']), reverse=True)[:10]
            
            # Filter products recommended for the user's gender
            if gender:
                recommended_for_gender = [p for p in all_products if p['recomendado_para'] == gender]
                products['recommended'] = random.sample(recommended_for_gender, min(len(recommended_for_gender), 15))

    except FileNotFoundError:
        return HttpResponse("Products file not found")
    
    return render(request, 'products.html', {
        'on_offer': products['on_offer'],
        'popular': products['popular'],
        'recommended': products['recommended']
    })

def category_products(request, category):
    try:
        with open(PRODUCTS_FILE_PATH, 'r') as csvfile:
            reader = csv.DictReader(csvfile)
            filtered_products = [product for product in reader if product['categoria'] == category]
            
            # Sort by popularity
            top_popular = sorted(filtered_products, key=lambda row: int(row['me_gusta']), reverse=True)[:5]
            
            # Sort by price and get the 5 cheapest
            cheapest = sorted(filtered_products, key=lambda row: float(row['precio']))[:5]
            
            # First 20 products
            product_list = filtered_products[:20]

    except FileNotFoundError:
        return HttpResponse("Products file not found")

    return render(request, 'category_products.html', {
        'category': category,
        'top_popular': top_popular,
        'cheapest': cheapest,
        'product_list': product_list
    })
