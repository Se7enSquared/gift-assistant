from pickletools import read_uint1
from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm as authform


from .models import Recipient, Gift
# from .forms import RecipientForm


def home(request):
    if request.user.is_authenticated:
        # TODO: Remove this comment before production
        # To see the homepage like a logged out user,
        # change 'welcome' to 'home' and refresh
        # the '' route
        return render(request, 'home.html')
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
