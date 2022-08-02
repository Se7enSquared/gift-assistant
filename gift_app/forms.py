from datetime import date
import calendar
from django import forms
from django.forms import ModelForm
from .models import Occasion, Recipient, Gift, CURRENT_YEAR


class RecipientForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['age'].help_text = '(approximate age if unknown)'

    # BOB: There are multiple issues with this code... Mainly -
    # the ValueError from the day being the wrong value (for exmaple "43")
    # is actually raised when calculate_age endpoint is called.
    # I want to validate the birth day value as soon as its entered, but
    # if the month is februrary, I can't know that until the year is added
    # So I think I wasted my time with this code because the date time module
    # should take care of it, which I knew but I was trying different things
    # I'm just leaving this code here for tonight to show what I was doing
    # Even though it is wrong
    # Next todo: figure out how to raise an error to a form through a view!
    # I am out of time so can't research this tonight
    @staticmethod
    def _validate_day(clean_data):
        month = clean_data['birth_month']
        day = clean_data['birth_day']
        year = clean_data['birth_year']

        if month == 2:
            return day <= 29 if calendar.isleap(year) else day <= 28
        if month in (4, 6, 9, 11):
            return day <= 30
        return day <= 31

    @staticmethod
    def _create_birthday(clean_data):
        day = clean_data['birth_day']
        month = clean_data['birth_month']
        year = clean_data['birth_year']
        try:
            return date(year, month, day)
        except ValueError:
            return False

    # here I removed your call to super().clean() or whatever it was before
    # because I was experimenting again. I had noticed that I was able to get
    # the data without that and just using self.cleaned_data. Let me know if
    # that was wrong. Thanks!
    def clean(self):
        if not self._create_birthday(self.cleaned_data):
            raise forms.ValidationError('Invalid Birthday')

    # again you can see here I was experimenting. I learned
    # the difference between form level and field level validation
    def clean_birth_day(self):
        if not self._validate_day(self.cleaned_data):
            raise forms.ValidationError('Invalid day')
        return

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
