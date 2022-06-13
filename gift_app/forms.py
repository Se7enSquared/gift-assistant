from django.forms import ModelForm

from .models import Occasion, Recipient, Gift


class RecipientForm(ModelForm):
    class Meta:
        model = Recipient
        fields = [
            "first_name",
            "last_name",
            "birth_date",
            "email",
            "relationship",
            "gender",
            "notes",
        ]


class OccasionForm(ModelForm):
    class Meta:
        model = Occasion
        fields = [
            "recipient",
            "name",
            "occasion_type",
            "repeat_yearly",
            "occasion_date",
            "description",
        ]


class GiftForm(ModelForm):
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
            "recipient",
        ]
