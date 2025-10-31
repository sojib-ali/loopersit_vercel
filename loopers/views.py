from django.shortcuts import render, get_object_or_404
from .models import Service, Review,Page, Pricing
from about.models import ProjectSummary



def home_page(request):
    services = Service.objects.all()
    reviews = Review.objects.all()[:3]
    summaries = ProjectSummary.objects.all()
    pricings = Pricing.objects.all()
    return render(request, 'loopers/home_page.html', {
        'services':services,
        'reviews': reviews,
        'summaries': summaries,
        'pricings':pricings})

def service(request):
    services = Service.objects.all()
    return render(request, 'loopers/service.html', {'active': 'service', 'services':services})

def sub_service(request, slug):
    service = get_object_or_404(Service, slug=slug)
    return render(request, 'loopers/sub_service.html', {'active': 'service', 'service':service})


def reviews(request):
    reviews = Review.objects.all()
    return render(request, 'loopers/reviews.html', {'active':'review', 'reviews':reviews})


def schedule(request):
    return render(request, 'loopers/schedule.html', {'active':'contact'})

def extra_page(request, slug):
    page = get_object_or_404(Page, slug=slug)
    return render(request, 'loopers/extra_page.html', {'page':page})

