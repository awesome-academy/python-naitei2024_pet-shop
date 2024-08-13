import re
from django.shortcuts import render, redirect, get_object_or_404
from django.utils.translation import gettext_lazy as _
from django.contrib import messages
from .forms import SignInForm
from django.contrib.auth import login, authenticate
from django.urls import reverse
from .models import *
from django.http import JsonResponse


def index(request):
    """View function for home page of site."""
    return render(request, "home.html")


def ShopView(request):
    """View function for shop page of site."""
    return render(request, "app/shop.html")


def clean_message(message):
    return re.sub('<[^<]+?>', '', str(message))


def login_view(request):
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    if user.is_banned:
                        messages.error(request, _(
                            "Your account has been banned."))
                    else:
                        login(request, user)
                        messages.success(request, _(
                            "You have been logged in successfully."))
                        return redirect('index')
                else:
                    request.session['user_id'] = user.id
                    return redirect(reverse('otp_verify'))
            else:
                messages.error(request, _("Invalid username or password."))
        else:
            for error in list(form.errors.values()):
                messages.error(request, clean_message(error))
    else:
        form = SignInForm()

    return render(request, 'registration/sign_in.html', {'form': form})


def get_price(request):
    if request.method == 'GET':
        size = request.GET.get('size')
        color = request.GET.get('color')
        price = get_price_from_database(size, color)

        if price is not None:
            return JsonResponse({'price': price})
        else:
            return JsonResponse({'price': None})
    return JsonResponse({'error': 'Invalid request method'}, status=400)


def get_available_options(request):
    if request.method == 'GET':
        available_sizes = ProductDetail.objects.values_list('size', flat=True).distinct()
        available_colors = ProductDetail.objects.values_list('color', flat=True).distinct()

        sizes = list(available_sizes)
        colors = list(available_colors)
        return JsonResponse({'sizes': sizes, 'colors': colors})
    return JsonResponse({'error': 'Invalid request method'}, status=400)


def get_price_from_database(size, color):
    try:
        product_detail = ProductDetail.objects.get(size=size, color=color)
        return product_detail.price
    except ProductDetail.DoesNotExist:
        return None


def product_detail_view(request, id):
    product = get_object_or_404(Product, pk=id)
    product_details = ProductDetail.objects.filter(product=product)
    average_rating = product.average_rating
    review_count = product.review_count
    sizes = product_details.values_list('size', flat=True).distinct()
    colors = product_details.values_list('color', flat=True).distinct()
    category = product.category
    comments = Comment.objects.filter(product=product).select_related('user')

    context = {
        "product": product,
        "category": category,
        "sizes": sizes,
        "colors": colors,
        "comments": comments,
        "average_rating": average_rating,
        "review_count": review_count,  # Sử dụng review_count từ property
    }
    return render(request, "product_detail.html", context)
