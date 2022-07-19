from django.test import TestCase
from gift_app.models import Recipient, Occasion


class RecipientTestCase(TestCase):
    def setUp(self):
        Recipient.objects.create(first_name='test_first',
                                 last_name='test_last',
                                 birth_month=11,
                                 birth_day=13,
                                 birth_year=1987,
                                 relationship='Other',
                                 gender='Male')

    def test_mother_day_added(self):
        mother = Recipient.objects.create(first_name='mother_first',
                                          last_name='mother_last',
                                          birth_month=10,
                                          birth_day=3,
                                          birth_year=1977,
                                          relationship='Parent',
                                          gender='Female')

        occasions = Occasion.objects.all()
        exists = False
        for occ in occasions:
            exists = occ.recipient == mother.id
        self.assertTrue(exists)
