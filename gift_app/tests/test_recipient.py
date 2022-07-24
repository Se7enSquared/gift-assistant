from datetime import date
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from gift_app.models import Recipient, Gift, Occasion
from gift_app.occasions import AutomateOccasions


class TestRecipientViews(TestCase):

    def setUp(self):
        self.recipient_url = reverse('recipients')
        self.recipient_list_url = reverse('recipient_list')
        self.recipient_add_url = reverse('recipient_add')
        self.recipient_edit_url = reverse('recipient_edit', args=[1])

        self.client = Client()
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()
        self.client.login(username='testuser', password='12345')

        self.generic_data = {
            'first_name': 'generic_first',
            'last_name': 'generic_last',
            'birth_month': 5,
            'birth_day': 4,
            'birth_year': 1966,
            'age': 0,
            'relationship': 'Other',
            'gender': 'Male'
        }

        self.edit_data = {
            'first_name': 'edit_first',
            'last_name': 'edit_last',
            'birth_month': 1,
            'birth_day': 3,
            'birth_year': 1980,
            'age': 17,
            'relationship': 'Child',
            'gender': 'Female'
        }

        self.mother_data = {
            'first_name': 'mother_first',
            'last_name': 'mother_last',
            'birth_month': 5,
            'birth_day': 4,
            'birth_year': 1966,
            'age': 0,
            'relationship': 'Parent',
            'gender': 'Female'
        }

        self.father_data = {
            'first_name': 'father_first',
            'last_name': 'father_last',
            'birth_month': 5,
            'birth_day': 4,
            'birth_year': 1966,
            'age': 0,
            'relationship': 'Parent',
            'gender': 'Male'
        }

        self.mother_object = Recipient.objects.create(
            first_name='test recipient first',
            last_name='test recipient last',
            birth_month=10,
            birth_day=3,
            birth_year=1960,
            relationship='Parent',
            gender='Female',
            user=user
        )

    def test_recipient_POST(self):
        self.client.post(self.recipient_add_url, data=self.generic_data)
        recipients = Recipient.objects.all()
        exists = any(
            recipient.first_name == 'generic_first'
            for recipient in recipients
        )
        self.assertTrue(exists)

    # QUESTION: Need help with this. I am getting a 404 error :()
    def test_recipient_edit(self):
        pk = self.mother_object.id
        response = self.client.post(self.recipient_edit_url,
                                    data=self.edit_data)
        self.assertEqual(response.status_code, 204)

        recipient = Recipient.objects.first()
        self.assertEqual(recipient.first_name, 'edit_first')
        self.assertEqual(recipient.last_name, 'edit_last')
        self.assertEqual(recipient.relationship, 'Child')

    def test_recipients_GET(self):  # sourcery skip: class-extract-method
        response = self.client.get(self.recipient_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'recipients/recipients.html')

    def test_recipient_list_GET(self):
        response = self.client.get(self.recipient_list_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,
                                'recipients/recipient_list.html')

    def test_mother_occasion_added(self):
        self.client.post(self.recipient_add_url, data=self.mother_data)
        occasions_list = Occasion.objects.all()
        exists = any(
            f'{occ.recipient.first_name} {occ.recipient.last_name}' ==
            'mother_first mother_last'
            for occ in occasions_list
        )
        self.assertTrue(exists)

    def test_father_occasion_added(self):
        self.client.post(self.recipient_add_url, data=self.father_data)
        occasions_list = Occasion.objects.all()
        exists = any(
            f'{occ.recipient.first_name} {occ.recipient.last_name}' ==
            'father_first father_last'
            for occ in occasions_list
        )
        self.assertEqual(exists, True)

    def test_auto_occasion(self):
        today = date(2022, 7, 20)
        mothers_day_2023 = date(2023, 5, 14)
        auto_occasion = AutomateOccasions(self.mother_object, today)
        auto_occasion.process_occasions()
        occasions = Occasion.objects.all()

        occ_date = None
        for occ in occasions:
            if occ.recipient == self.mother_object:
                occ_date = occ.occasion_date

        self.assertEqual(occ_date, mothers_day_2023)
