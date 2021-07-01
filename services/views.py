from django.shortcuts import render, redirect, reverse, get_object_or_404, HttpResponse
from django.contrib import messages 
# from .services import forms


"""view-link to return our services menu on main-nav bar"""


def our_services(request):
    """ A view to our services page """

    return render(request, 'services/our_services.html')


def brands(request):
    """ A view to brands page """

    return render(request, 'services/brands.html')


def about(request):
    """ view to return the about page """

    return render(request, 'services/about.html')


def our_brands(request):
    """ A view to our_brands page """

    return render(request, 'services/our_brands.html')


def contact(request, methods=["GET", "POST"]):
    """ A view to contact us page """
    request.GET

    return render(request, 'services/contact.html')

    """ view-link to return about us menu on main-nav bar"""


def graphic_design(request):
    """ A view to graphic design page """

    return render(request, 'services/graphic_design.html')


def web_design(request):
    """ A view to web design page """

    return render(request, 'services/web_design.html')


def web_development(request):
    """ A view to web developmnet page """

    return render(request, 'services/web_development.html')


def digital_marketing(request):
    """ A view to digital marketing page """

    return render(request, 'services/digital_marketing.html')


def calculator(request):
    """ A view to show a calculator page """

    return render(request, 'services/calculator.html')
