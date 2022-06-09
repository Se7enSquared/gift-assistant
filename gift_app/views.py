from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


from .models import Recipient, Gift


def home(request):
    if request.user.is_authenticated:
        return render(request, 'welcome.html')
    return render(request, 'home.html')


def recipient_list(request):
    return render(request, 'recipients.html', {
        'recipients': Recipient.objects.all()})


def recipient_detail(request):
    pass


def recipient_add(request):
    pass


def recipient_edit(request):
    pass


def recipient_delete(request):
    pass


def gift_list(request):
    return render(request, 'gifts.html', {'gifts': Gift.objects.all()})
