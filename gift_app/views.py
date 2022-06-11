from django.http import HttpResponse
from django.shortcuts import render


from .models import Recipient, Gift
from .forms import RecipientForm


def home(request):
    if request.user.is_authenticated:
        return render(request, 'welcome.html')
    return render(request, 'home.html')


def recipients(request):
    return render(request, 'recipients.html')


def recipient_list(request):
    return render(request, 'recipient_list.html', {
        'recipients': Recipient.objects.all()})


def recipient_detail(request):
    pass


def recipient_add(request):
    if request.method == "POST":
        form = RecipientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204,
                                headers={'HX-Trigger': 'recipientListChanged'})
    else:
        form = RecipientForm()
    return render(request, 'recipient_form.html', {
        'form': form,
    })


def recipient_edit(request):
    pass


def recipient_delete(request):
    pass


def gift_list(request):
    return render(request, 'gifts.html', {'gifts': Gift.objects.all()})
