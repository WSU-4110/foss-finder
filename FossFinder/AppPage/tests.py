from django.test import TestCase
from django.urls import reverse
from .views import ImageUrlParser
"""
class NavigationBarTest(TestCase):
    def test_homepage(self):
        response = self.client.get(reverse('software_index'))
        self.assertEqual(response.status_code, 200)
    def test_aboutpage(self):
        response = self.client.get(reverse('about'))
        self.assertEqual(response.status_code, 200)
    def test_softwaresubmission(self):
        response = self.client.get(reverse('software_submit'))
        self.assertEqual(response.status_code, 200)
    def test_reportbugs(self):
        response = self.client.get(reverse('bug_report'))
        self.assertEqual(response.status_code, 200)
"""
class ImageUrlParserTestCase(TestCase):

    """Dog Test"""
    def test_get_image_filename_from_url(self):
        image_url = 'https://picsum.photos/id/237/200/300.jpg'
        filename = ImageUrlParser.get_image_filename_from_url(image_url)
        self.assertEqual(filename, '300.jpg')

    