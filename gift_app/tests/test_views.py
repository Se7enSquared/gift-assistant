from datetime import date
from django.contrib.auth.models import User
from django.test import TestCase, Client
from django.urls import reverse
from gift_app.models import Recipient, Gift, Occasion
import json

from gift_app.occasions import AutomateOccasions


class TestRecipientViews(TestCase):

    def setUp(self):
        self.recipient_url = reverse('recipients')
        self.recipient_list_url = reverse('recipient_list')
        self.recipient_add_url = reverse('recipient_add')

        self.client = Client()

        users = User.objects.all()
        if 'testuser' not in users:
            user = User.objects.create(username='testuser')
            user.set_password('12345')
            user.save()

        self.mother = Recipient.objects.create(
            first_name='test recipient first',
            last_name='test recipient last',
            birth_month=10,
            birth_day=3,
            birth_year=1960,
            relationship='Parent',
            gender='Female'
        )

        self.occasions_list = Occasion.objects.all()


    def test_recipients_GET(self):  # sourcery skip: class-extract-method
        if self.client.login(username='testuser', password='12345'):
            response = self.client.get(self.recipient_url)

            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response,
                                    'recipients/recipients.html')

    def test_recipient_list_GET(self):
        if self.client.login(username='testuser', password='12345'):
            response = self.client.get(self.recipient_list_url)

            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response,
                                    'recipients/recipient_list.html')

    def test_auto_occasion_added(self):
        if self.client.login(username = 'testuser', password = '12345'):
            exists = any(occ.recipient == self.mother for occ in self.occasions_list)
            self.assertEqual(exists, True)

    def test_auto_occasion(self):
        if self.client.login(username='testuser', password='12345'):
            #breakpoint()
            today = date(2022, 7, 20)
            mothers_day_2023 = date(2023, 5, 14)
            occ_date = None
            auto_occasion = AutomateOccasions(self.mother, today)
            auto_occasion.process_occasions()
            occasions = Occasion.objects.all()

            for occ in occasions:
                if occ.recipient == self.mother:
                    occ_date = occ.occasion_date

            self.assertEqual(occ_date, mothers_day_2023)
