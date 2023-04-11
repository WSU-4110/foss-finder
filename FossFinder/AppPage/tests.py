from django.test import TestCase
from django.urls import reverse

class NavigationBarTest(TestCase):
    def test_navigation_bar(self):
        response = self.client.get(reverse('software_index'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('software_submit'))
        self.assertEqual(response.status_code, 200)

        response = self.client.get(reverse('bug_report'))
        self.assertEqual(response.status_code, 200)
