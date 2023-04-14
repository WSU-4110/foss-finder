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