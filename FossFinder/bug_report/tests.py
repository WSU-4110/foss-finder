from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import SubmitBugsForm
from .models import SubmittedBugs


class SubmitBugsFormTest(TestCase):
    def test_valid_form(self):
        # create a test image file
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        
        form_data = {
          'title': 'Test Bug', 
           'description': 'This is a test bug', 
            'image': image
        }
        form = SubmitBugsForm(data=form_data, files=form_data)
        
        self.assertTrue(form.is_valid())
        
        # test saving the form
        form.save()
        self.assertEqual(SubmittedBugs.objects.count(), 1)
        
    def test_invalid_form(self):
        image = SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg")
        form_data = {
        'description': 'This is a test bug report.',
        'image': image
    }
        form = SubmitBugsForm(data=form_data, files=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors)