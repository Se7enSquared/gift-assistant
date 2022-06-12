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
    recipients = Recipient.objects.filter(user=request.user)
    return render(request, 'recipient_list.html',
                  {'recipients': recipients})


def recipient_detail(request):
    pass


def recipient_add(request):
    if request.method == "POST":
        form = RecipientForm(request.POST)
        if form.is_valid():
            recipient = form.save(commit=False)
            recipient.user = request.user
            recipient.save()
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


def gifts(request):
    return render(request, 'gifts.html')


def gift_list(request):
    return render(request, 'gift_list.html',
                  {'gifts': Gift.objects.all()})


def gift_detail(request):
    pass


def gift_add(request):
    if request.method == "POST":
        form = RecipientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse(status=204,
                                headers={'HX-Trigger': 'giftListChanged'})
    else:
        form = RecipientForm()
    return render(request, 'gift_form.html', {
        'form': form,
    })


def gift_edit(request):
    pass


def gift_delete(request):
    pass
