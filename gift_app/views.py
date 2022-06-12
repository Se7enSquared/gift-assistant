from django.http import HttpResponse
from django.shortcuts import render


from .models import Recipient, Gift, Occasion
from .forms import RecipientForm, OccasionForm


def home(request):
    if request.user.is_authenticated:
        return render(request, 'welcome.html')
    return render(request, 'home.html')


def recipients(request):
    return render(request, 'recipients.html')


def recipient_list(request):
    return render(request, 'recipient_list.html',
                  {'recipients': Recipient.objects.all()})


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


def occasions(request):
    return render(request, 'occasions.html')


def occasion_list(request):
    return render(request, 'occasion_list.html',
                  {'occasions': Occasion.objects.all()})


def occasion_add(request):
    if request.method == "POST":
        form = OccasionForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204,
                                headers={'HX-Trigger': 'occasionListChanged'})
    else:
        form = OccasionForm()
    return render(request, 'occasion_form.html', {
        'form': form,
    })

def occasion_edit(request):
    pass


def occasion_delete(request):
    pass