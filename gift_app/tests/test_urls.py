from django.test import SimpleTestCase
from django.urls import reverse, resolve
from gift_app.views import recipient_list, occasion_list, gift_list


class TestUrls(SimpleTestCase):

    def test_recipient_list_url_is_resolved(self):
        url = reverse('recipient_list')
        self.assertEquals(resolve(url).func, recipient_list)

    def test_occasion_list_url_is_resolved(self):
        url = reverse('occasion_list')
        self.assertEquals(resolve(url).func, occasion_list)

    def test_gift_list_url_is_resolved(self):
        url = reverse('gift_list')
        self.assertEquals(resolve(url).func, gift_list)
