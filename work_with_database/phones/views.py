from django.shortcuts import render, redirect
from phones.models import Phone


def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sort_field = request.GET.get('sort', '')
    phones_objects = Phone.objects.all()
    phones = [{'name': el.name, 'price': el.price, 'slug': el.slug,
               'image': el.image} for el in phones_objects]
    if sort_field == "name":
        phones.sort(key=lambda el: el['name'])
    elif sort_field == 'min_price':
        phones.sort(key=lambda el: el['price'])
    elif sort_field == 'max_price':
        phones.sort(key=lambda el: el['price'], reverse=True)

    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    el = Phone.objects.filter(slug=slug)[0]
    context = {'phone': {'name': el.name, 'price': el.price, 'slug': el.slug,
               'image': el.image, 'release_date': el.release_date, 'lte_exists': el.lte_exists

                         }}
    return render(request, template, context)
