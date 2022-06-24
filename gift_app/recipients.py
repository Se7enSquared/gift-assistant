from django import forms
from datetime import date
from gift_app.models import Recipient


class ValidateRecipient():

    def __init__(self, recipient):
        self.recipient = recipient

    def validate(self):
        self.validate_birthday()
        self.validate_age()
        self.is_not_duplicate()

    def validate_birthday(self):
        birth_year = self.recipient.birth_year

        if self.recipient.birth_month < 1 or self.recipient.birth_month > 12:
            raise forms.ValidationError('Invalid birth month')
        if self.recipient.birth_day < 1 or self.recipient.birth_day > 31:
            raise forms.ValidationError('Invalid birth day')
        if birth_year and (birth_year < 0 or birth_year > date.today().year):
            raise forms.ValidationError('Invalid birth year')

    def validate_age(self):
        if self.recipient.age < 0:
            raise forms.ValidationError('Invalid age')
        if self.recipient.age > 120:
            raise forms.ValidationError('Invalid age')

    def is_not_duplicate(self):
        if Recipient.objects.filter(
                first_name=self.recipient.first_name,
                last_name=self.recipient.last_name).exists():
            raise forms.ValidationError('Recipient already exists')

    def set_rel(self):
        return 'Other' if self.recipient.relationship == 'Select' else \
            self.recipient.relationship
