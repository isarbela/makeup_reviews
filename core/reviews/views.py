from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Product, Review
from .forms import ReviewForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.db.models import Q, Avg


def home(request):
    latest_products = Product.objects.all().order_by('-id')[:34]
    top_rated = Product.objects.annotate(average_rating = Avg('reviews__rating')).order_by('-average_rating')[:10]
    return render(request, 'home.html', {'latest_products': latest_products,'top_rated': top_rated})

def product_list(request):
    products = Product.objects.all()
    return render(request, 'reviews/product_list.html', {'products': products})

def product_detail(request, pk):
    product = Product.objects.get(id=pk)
    reviews = Review.objects.filter(product=product)
    average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
    return render(request, 'reviews/product_detail.html', {'product': product, 'reviews': reviews, 'average_rating': average_rating})

@login_required
def add_review(request, pk):
    product = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.user = request.user
            review.product = product
            review.save()
            return redirect('product_detail', pk=pk)
    else:
        form = ReviewForm()
    return render(request, 'reviews/add_review.html', {'form':form})     

def about(request):
    context = {
        'page_title': 'Sobre Nós' 
    }
    return render(request, 'about_us.html', context)   

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'account/signup.html', {'form': form})

@login_required
def view_profile(request):
    return render(request, 'account/profile.html')

def logout_view(request):
    return render(request, 'account/logout.html')

def search_results(request):
    query = request.GET.get('query').strip()
    if query:
        products = Product.objects.filter(
            Q(name__icontains=query) | Q(brand__name__icontains=query)
        )
    else:
        products = []
    return render(request, 'search_results.html', {'products': products})