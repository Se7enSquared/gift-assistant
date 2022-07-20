from django.test import TestCase
from gift_app.models import Recipient, Occasion, Gift


class RecipientTestCase(TestCase):
    def setUp(self):
        self.test_recipient = Recipient.objects.create(first_name='test_first',
                                                       last_name='test_last',
                                                       birth_month=11,
                                                       birth_day=13,
                                                       birth_year=1987,
                                                       relationship='Other',
                                                       gender='Male')

        self.mother = Recipient.objects.create(first_name='mother_first',
                                               last_name='mother_last',
                                               birth_month=10,
                                               birth_day=3,
                                               birth_year=1977,
                                               relationship='Parent',
                                               gender='Female')

    def test_add_recipient(self):
        pass

    # Test Scenarios:
    # Adding a mother & a father - add mothers & fathers's days
    # Set a fixed datetime for testing

    # Other ToDo:
    # Automatically add birthday occasions
