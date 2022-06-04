from django.forms import ModelForm

from .models import Recipient


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
