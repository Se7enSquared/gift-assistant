from django.shortcuts import render


from .models import Recipient
from .forms import RecipientForm


def home(request):
    return render(request, 'home.html')


def recipient_list(request):
    recipients = Recipient.objects.all()
    return render(request, 'recipients.html', {
        'recipients': recipients})


def recipient_detail(request):
    pass


def recipient_add(request):
    pass


def recipient_edit(request):
    pass


def recipient_delete(request):
    pass
