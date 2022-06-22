from django import forms
from django.forms import ModelForm
from .models import Occasion, Recipient, Gift


class RecipientForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['age'].help_text = '(approximate age if unknown)'

    class Meta:
        model = Recipient
        fields = [
            "first_name",
            "last_name",
            "birth_month",
            "birth_day",
            "birth_year_unknown",
            "birth_year",
            "age",
            "email",
            "relationship",
            "gender",
            "notes",
        ]


class OccasionForm(ModelForm):

    occasion_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Occasion
        fields = [
            "recipient",
            "occasion_type",
            "repeat_yearly",
            "occasion_date",
            "description",
        ]


class GiftForm(ModelForm):
    date_given = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Gift
        fields = [
            "title",
            "description",
            "gift_type",
            "link",
            "given",
            "date_given",
            "occasion",
        ]
