from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render


from .models import Recipient, Gift, Occasion
from .forms import RecipientForm, OccasionForm, GiftForm


def home(request):
    if request.user.is_authenticated:
        return render(request, 'welcome.html')
    return render(request, 'home.html')


# R E C I P I E N T  V I E W S ------------------------>
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


# O C C A S I O N  V I E W S ------------------------>
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


# G I F T  V I E W S ------------------------>
def gifts(request):
    return render(request, 'gifts.html')


def gift_list(request):
    gifts = Gift.objects.filter(user=request.user)
    return render(request, 'gift_list.html',
                  {'gifts': gifts})


def gift_view(request, pk):
    gift = Gift.objects.get(pk=pk)
    form = GiftForm(request.GET)
    return render(request, 'gift_view.html', {'gift': gift, 'form': form})


def gift_add(request):
    recipients = Recipient.objects.filter(user=request.user)
    occasions = Occasion.objects.filter(user=request.user)
    if request.method == "POST":
        form = GiftForm(request.POST)
        context = {'form': form, 'recipients': recipients,
                   'occasions': occasions}
        if form.is_valid():
            gift = form.save(commit=False)
            gift.user = request.user
            gift.save()
            return HttpResponse(status=204,
                                headers={'HX-Trigger': 'giftListChanged'})
    else:
        form = GiftForm()
        context = {'form': form, 'recipients': recipients,
                   'occasions': occasions}

    return render(request, 'gift_form.html', context)


def gift_edit(request, pk):
    gift = get_object_or_404(Gift, pk=pk)
    if request.method == "POST":
        form = GiftForm(request.POST, instance=gift)
        context = {'form': form}
        if form.is_valid():
            gift = form.save(commit=False)
            gift.user = request.user
            gift.save()
            return HttpResponse(status=204,
                                headers={'HX-Trigger': 'giftListChanged'})
    else:
        form = GiftForm(instance=gift)
        context = {'form': form}
    return render(request, 'gift_edit.html', context)


def gift_delete(request):
    pass
