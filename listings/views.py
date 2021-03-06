from django.shortcuts import render, get_object_or_404
from .models import Listing
from django.core.paginator import Paginator
from realtors.models import Realtor
from .choices import bedroom_choices, price_choices, state_choices
# Create your views here.


def index(request):
    listings = Listing.objects.all()
    paginator = Paginator(listings, 3)
    page_num = request.GET.get('page')
    paged_listings = paginator.get_page(page_num)

    context = {'paged_listings':paged_listings}


    return render(request, 'listings/listings.html', context)

def listing(request, id):
    listing_obj = get_object_or_404(Listing, pk=id)
    #realtors = Realtor.objects.get(pk=id)

    context = {
        'listing': listing_obj,
        # 'realtor': realtors
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    listings = Listing.objects.order_by('-create_date')
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            listings = listings.filter(description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            listings = listings.filter(city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']
        if state:
            listings = listings.filter(state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            listings = listings.filter(bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            listings = listings.filter(price__lte=price)

    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
        'values': request.GET
    }
    return render(request, 'listings/search.html', context)


