from django.forms import ModelForm

from .models import Occasion, Recipient


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
