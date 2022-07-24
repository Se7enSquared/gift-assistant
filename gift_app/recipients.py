from django import forms
from datetime import date
from gift_app.models import Recipient

SELECT = 'Select'
OTHER = 'Other'
MIN_YEAR = 1900
MAX_AGE = 120


class ValidateRecipient():

    def __init__(self, recipient: Recipient):
        self.recipient = recipient

    def validate(self):
        self.validate_birthday()
        self.validate_age()
        self.is_not_duplicate()

    def validate_birthday(self):
        birth_year = self.recipient.birth_year

        if self.recipient.birth_day < 1 or self.recipient.birth_day > 31:
            raise forms.ValidationError('Invalid birth day')
        if birth_year and (birth_year < MIN_YEAR or birth_year > date.today().year):
            raise forms.ValidationError('Year must be an integer'
                                        f'between {MIN_YEAR}'
                                        f'and {date.today.year()}')

    def validate_age(self):
        if self.recipient.age is None:
            self.recipient.age = 0
        if self.recipient.age < 0:
            raise forms.ValidationError('Age must be a positive integer')
        if self.recipient.age > 120:
            raise forms.ValidationError(f'Age may not be more than {MAX_AGE}')

    def is_not_duplicate(self):
        if Recipient.objects.filter(
                first_name=self.recipient.first_name,
                last_name=self.recipient.last_name).exists():
            raise forms.ValidationError('Recipient already exists')

    def set_rel(self):
        return (OTHER if self.recipient.relationship == SELECT else
                self.recipient.relationship)
