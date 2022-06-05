from django.shortcuts import render


from .models import Recipient
from .forms import RecipientForm


def home(request):
    if request.user.is_authenticated:
        # TODO: Remove this comment before production
        # To see the homepage like a logged out user,
        # change 'welcome' to 'home'
        return render(request, 'welcome.html')
    else:
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
