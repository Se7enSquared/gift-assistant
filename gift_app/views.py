from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.db.models import Count
from gift_app.occasions import AutomatedOccasions

from .models import Recipient, Gift, Occasion
from .forms import RecipientForm, OccasionForm, GiftForm


def home(request):
    if request.user.is_authenticated:
        return render(request, 'welcome.html')
    return render(request, 'home.html')


# R E C I P I E N T  V I E W S ------------------------>
def recipients(request):
    return render(request, 'recipients/recipients.html')


def recipient_list(request):
    recipients = Recipient.objects.filter(
        user=request.user).annotate(Count('occasion'))
    return render(request, 'recipients/recipient_list.html',
                  {'recipients': recipients})


def recipient_add(request):
    recipients = Recipient.objects.filter(user=request.user)
    occasions = Occasion.objects.filter(user=request.user)
    if request.method == "POST":
        form = RecipientForm(request.POST)
        if form.is_valid():
            recipient = form.save(commit=False)
            recipient.user = request.user
            recipient.save()

            # this is kinda nice, maybe no signals anymore?
            ao = AutomatedOccasions(recipient)
            ao.process_occasions()

            return HttpResponse(status=204,
                                headers={'HX-Trigger': 'recipientListChanged'})
    else:
        form = RecipientForm()

    context = {'form': form, 'recipients': recipients,
               'occasions': occasions}
    return render(request, 'recipients/recipient_form.html', context)


def recipient_edit(request, pk):
    recipient = get_object_or_404(Recipient, pk=pk, user=request.user)
    if request.method == "POST":
        form = RecipientForm(request.POST, instance=recipient)
        if form.is_valid():
            recipient = form.save(commit=False)
            recipient.user = request.user
            recipient.save()
            return HttpResponse(status=204,
                                headers={'HX-Trigger': 'recipientListChanged'})
    else:
        form = RecipientForm(instance=recipient)

    context = {'form': form}
    return render(request, 'recipients/recipient_edit.html', context)


def recipient_delete(request, pk):
    recipient = get_object_or_404(Recipient, pk=pk, user=request.user)

    if request.method == 'POST':
        recipient.delete()
        return HttpResponse(status=204,
                            headers={'HX-Trigger': 'recipientListChanged'})
    else:
        return render(request, 'recipients/recipient_delete.html', {'recipient': recipient})


# O C C A S I O N  V I E W S ------------------------>
def occasions(request):
    return render(request, 'occasions/occasions.html')


def occasion_list(request):
    occasions = Occasion.objects.filter(user=request.user)
    return render(request, 'occasions/occasion_list.html',
                  {'occasions': occasions})


def occasion_add(request):
    occasions = Occasion.objects.filter(user=request.user)
    occasions = Occasion.objects.filter(user=request.user)
    if request.method == "POST":
        form = OccasionForm(request.POST)
        if form.is_valid():
            occasion = form.save(commit=False)
            occasion.user = request.user
            occasion.save()
            return HttpResponse(status=204,
                                headers={'HX-Trigger': 'occasionListChanged'})
    else:
        form = OccasionForm()

    context = {'form': form, 'occasions': occasions,
               'occasions': occasions}
    return render(request, 'occasions/occasion_form.html', context)


def occasion_edit(request, pk):
    occasion = get_object_or_404(Occasion, pk=pk, user=request.user)
    if request.method == "POST":
        form = OccasionForm(request.POST, instance=occasion)
        if form.is_valid():
            occasion = form.save(commit=False)
            occasion.user = request.user
            occasion.save()
            return HttpResponse(status=204,
                                headers={'HX-Trigger': 'occasionListChanged'})
    else:
        form = OccasionForm(instance=occasion)

    context = {'form': form}
    return render(request, 'occasions/occasion_edit.html', context)


def occasion_delete(request, pk):
    occasion = get_object_or_404(Occasion, pk=pk, user=request.user)

    if request.method == 'POST':
        occasion.delete()
        return HttpResponse(status=204,
                            headers={'HX-Trigger': 'occasionListChanged'})
    else:
        return render(request, 'occasions/occasion_delete.html',
                      {'occasion': occasion})

# G I F T  V I E W S ------------------------>


def gifts(request):
    return render(request, 'gifts/gifts.html')


def gift_list(request):
    gifts = Gift.objects.filter(user=request.user)
    return render(request, 'gifts/gift_list.html',
                  {'gifts': gifts})


def gift_add(request):
    recipients = Recipient.objects.filter(user=request.user)
    occasions = Occasion.objects.filter(user=request.user)
    if request.method == "POST":
        form = GiftForm(request.POST)
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
    return render(request, 'gifts/gift_form.html', context)


def gift_edit(request, pk):
    gift = get_object_or_404(Gift, pk=pk, user=request.user)
    if request.method == "POST":
        form = GiftForm(request.POST, instance=gift)
        if form.is_valid():
            gift = form.save(commit=False)
            gift.user = request.user
            gift.save()
            return HttpResponse(status=204,
                                headers={'HX-Trigger': 'giftListChanged'})
    else:
        form = GiftForm(instance=gift)

    context = {'form': form}
    return render(request, 'gifts/gift_edit.html', context)


def gift_delete(request, pk):
    gift = get_object_or_404(Gift, pk=pk, user=request.user)

    if request.method == 'POST':
        gift.delete()
        return HttpResponse(status=204,
                            headers={'HX-Trigger': 'giftListChanged'})
    else:
        return render(request, 'gifts/gift_delete.html', {'gift': gift})
