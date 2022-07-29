from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.db.models import Count
from gift_app.occasions import AutomateOccasions
from gift_app.recipients import ValidateRecipient
from django.contrib.auth.decorators import login_required

from .models import Recipient, Gift, Occasion
from .forms import RecipientForm, OccasionForm, GiftForm


def home(request: HttpRequest):
    if request.user.is_authenticated:
        return render(request, 'welcome.html')
    return render(request, 'home.html')


# R E C I P I E N T  V I E W S ------------------------>
@login_required
def recipients(request: HttpRequest):
    return render(request, 'recipients/recipients.html')


@login_required
def recipient_list(request: HttpRequest):
    recipients = Recipient.objects.filter(
        user=request.user).annotate(Count('occasion'))
    return render(request, 'recipients/recipient_list.html',
                  {'recipients': recipients})


@login_required
def recipient_add(request: HttpRequest):
    recipients = Recipient.objects.filter(user=request.user)
    occasions = Occasion.objects.filter(user=request.user)

    if request.method == "POST":
        form = RecipientForm(request.POST)

        if form.is_valid():
            recipient = form.save(commit=False)
            recipient.user = request.user
            recipient_validation = ValidateRecipient(recipient)
            recipient_validation.validate()
            recipient.save()
            auto_occasion = AutomateOccasions(recipient)
            auto_occasion.process_occasions()
            return HttpResponse(status=204,
                                headers={'HX-Trigger': 'recipientListChanged'})
        else:
            context = {'form': form, 'recipients': recipients,
                       'occasions': occasions}
            return render(request, 'recipients/recipient_form.html',
                          {'form': form, 'recipients': recipients, 'occasions': occasions})
    else:
        form = RecipientForm()

    context = {'form': form, 'recipients': recipients,
               'occasions': occasions}
    return render(request, 'recipients/recipient_form.html', context)


@login_required
def recipient_edit(request: HttpRequest, pk: int) -> HttpResponse:
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


@login_required
def recipient_delete(request: HttpRequest, pk: int) -> HttpResponse:
    recipient = get_object_or_404(Recipient, pk=pk, user=request.user)

    if request.method != 'POST':
        return render(request, 'recipients/recipient_delete.html', {'recipient': recipient})
    recipient.delete()
    return HttpResponse(status=204,
                        headers={'HX-Trigger': 'recipientListChanged'})


# O C C A S I O N  V I E W S ------------------------>
@login_required
def occasions(request: HttpRequest) -> HttpResponse:
    return render(request, 'occasions/occasions.html')


@login_required
def occasion_list(request: HttpRequest) -> HttpResponse:
    occasions = Occasion.objects.filter(user=request.user)
    return render(request, 'occasions/occasion_list.html',
                  {'occasions': occasions})


@login_required
def occasion_add(request: HttpRequest) -> HttpResponse:
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


@login_required
def occasion_edit(request: HttpRequest, pk: int) -> HttpResponse:
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


@login_required
def occasion_delete(request: HttpRequest, pk: int) -> HttpResponse:
    occasion = get_object_or_404(Occasion, pk=pk, user=request.user)

    if request.method != 'POST':
        return render(request, 'occasions/occasion_delete.html',
                      {'occasion': occasion})
    occasion.delete()
    return HttpResponse(status=204,
                        headers={'HX-Trigger': 'occasionListChanged'})


# G I F T  V I E W S ------------------------>

@login_required
def gifts(request: HttpRequest) -> HttpResponse:
    return render(request, 'gifts/gifts.html')


@login_required
def gift_list(request: HttpRequest) -> HttpResponse:
    gifts = Gift.objects.filter(user=request.user)
    return render(request, 'gifts/gift_list.html',
                  {'gifts': gifts})


@login_required
def gift_add(request: HttpRequest) -> HttpResponse:
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


@login_required
def gift_edit(request: HttpRequest, pk: int) -> HttpResponse:
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


@login_required
def gift_delete(request: HttpRequest, pk: int) -> HttpResponse:
    gift = get_object_or_404(Gift, pk=pk, user=request.user)

    if request.method != 'POST':
        return render(request, 'gifts/gift_delete.html', {'gift': gift})
    gift.delete()
    return HttpResponse(status=204,
                        headers={'HX-Trigger': 'giftListChanged'})


@login_required
def calculate_age(request, year, month, day):
    age = Recipient.calculate_age(year, month, day)
    return JsonResponse({"age": age})
