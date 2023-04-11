from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .forms import SubmitBugsForm
from .models import SubmittedBugs


class SubmitBugsFormTest(TestCase):
    def valid_test(self):
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
        
        def invalid_test(self):
    form_data = {
        'description': 'This is a test bug report.',
        'image': self.test_image,
    }
    form = SubmitBugsForm(data=form_data, files=self.form_files)
    self.assertFalse(form.is_valid())
    self.assertEqual(len(form.errors), 1)
    self.assertIn('title', form.errors)

