import urllib
from django.shortcuts import render
from AppPage.models import Software
from django.test import TestCase
from SoftwareSubmissionPage.models import SubmittedSoftware
from urllib.parse import urlparse

class ImageUrlParser:
    @staticmethod
    def get_image_filename_from_url(image_url):
        """
        Extracts the image filename from the given image URL.

        Args:
            image_url (str): The URL of the image.

        Returns:
            str: The filename of the image.
        """
        parsed_url = urlparse(image_url)
        filename = parsed_url.path.split('/')[-1]
        return filename

    @staticmethod
    def is_valid_image_url(image_url):
        """
        Checks if the given URL is a valid image URL.

        Args:
            image_url (str): The URL to check.

        Returns:
            bool: True if the URL is a valid image URL, False otherwise.
        """
        valid_extensions = ['.jpg', '.jpeg', '.png', '.gif']
        parsed_url = urlparse(image_url)
        file_extension = parsed_url.path[-4:]
        return file_extension.lower() in valid_extensions

    @staticmethod
    def get_image_extension_from_url(image_url):
        """
        Extracts the image file extension from the given image URL.

        Args:
            image_url (str): The URL of the image.

        Returns:
            str: The file extension of the image.
        """
        parsed_url = urlparse(image_url)
        file_extension = parsed_url.path[-4:]
        return file_extension.lower()
    


    @staticmethod
    def is_external_image_url(image_url):
        """
        Checks if the given URL is an external image URL (i.e., not from the same domain as the current Django app).

        Args:
            image_url (str): The URL to check.

        Returns:
            bool: True if the URL is an external image URL, False otherwise.
        """
        parsed_url = urlparse(image_url)
        return parsed_url.netloc != ''

    @staticmethod
    def get_image_domain(image_url):
        """
        Extracts the domain from the given image URL.

        Args:
            image_url (str): The URL of the image.

        Returns:
            str: The domain of the image URL.
        """
        parsed_url = urlparse(image_url)
        return parsed_url.netloc

    @staticmethod
    def is_secure_image_url(image_url):
        """
        Checks if the given image URL uses HTTPS (secure) protocol.

        Args:
            image_url (str): The URL to check.

        Returns:
            bool: True if the URL uses HTTPS, False otherwise.
        """
        parsed_url = urlparse(image_url)
        return parsed_url.scheme == 'https'

class ImageUrlParserTestCase(TestCase):

    """Dog Test"""
    def test_get_image_filename_from_url(self):
        image_url = 'https://picsum.photos/id/237/200/300'
        filename = ImageUrlParser.get_image_filename_from_url(image_url)
        self.assertEqual(filename, 'image.jpg')

    """Ice Test"""
    def test_is_valid_image_url(self):
        valid_image_url = 'https://picsum.photos/seed/picsum/200/300'
        invalid_image_url = 'https://example.com/files/document.pdf'
        self.assertTrue(ImageUrlParser.is_valid_image_url(valid_image_url))
        self.assertFalse(ImageUrlParser.is_valid_image_url(invalid_image_url))

    
    """Walrus Grayscale Test"""
    def test_get_image_extension_from_url(self):
        image_url = 'https://picsum.photos/200/300?grayscale'
        extension = ImageUrlParser.get_image_extension_from_url(image_url)
        self.assertEqual(extension, '.jpg')

    """Dog Test for External Image"""
    def test_is_external_image_url(self):
        external_image_url = 'https://picsum.photos/id/237/200/300'
        internal_image_url = '/images/image.jpg'
        self.assertTrue(ImageUrlParser.is_external_image_url(external_image_url))
        self.assertFalse(ImageUrlParser.is_external_image_url(internal_image_url))

    """Dog Test for acquiring Image Domain"""
    def test_get_image_domain(self):
        image_url = 'https://picsum.photos/id/237/200/300'
        domain = ImageUrlParser.get_image_domain(image_url)
        self.assertEqual(domain, 'example.com')

    """Dog Test for Ensuring Image URL is Secure"""
    def test_is_secure_image_url(self):
        secure_image_url = 'https://picsum.photos/seed/picsum/200/300'
        insecure_image_url = 'http://picsum.photos/seed/picsum/200/300'
        self.assertTrue(ImageUrlParser.is_secure_image_url(secure_image_url))
        self.assertFalse(ImageUrlParser.is_secure_image_url(insecure_image_url))

def software_index(request):
    software = Software.objects.all()
    context = {
        'Software': software
    }
    return render(request, 'software_index.html', context)

def software_detail(request, pk):
    software = Software.objects.get(pk=pk)
    context = {
        'Software': software
    }
    return render(request, 'software_detail.html', context)