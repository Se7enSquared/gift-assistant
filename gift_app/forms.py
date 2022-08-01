import re
from django import forms
from django.forms import ModelForm
from .models import Occasion, Recipient, Gift


class RecipientForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['age'].help_text = '(approximate age if unknown)'

    def clean(self):
        cleaned_data = super().clean()
        if cleaned_data["birth_day"] is not None:
            bday = int(cleaned_data["birth_day"])
            # TODO: use datetime because Feb has 28 (or 29) days
            if bday < 1 or bday > 31:
                raise forms.ValidationError("birth day is wrong")

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
            "relationship",
            "gender",
            "notes",
        ]


class OccasionForm(ModelForm):

    occasion_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}), required=False)

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
        widget=forms.DateInput(attrs={'type': 'date'}), required=False)

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
