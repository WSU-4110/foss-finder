from django.test import TestCase
from django.core.files.uploadedfile import SimpleUploadedFile
from .models import SubmittedBugs
from .forms import SubmitBugsForm

class BugSubmissionFormTest(TestCase):

    def test_missing_title(self):
        form_data = {
            'description': 'Test Bug Description',
            'image': SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg"),
        }
        form = SubmitBugsForm(data=form_data, files=form_data)
        self.assertEqual(form.errors['title'], ['This field is required.'])

    def test_missing_description(self):
        form_data = {
            'title': 'Test Bug Title',
            'image': SimpleUploadedFile("test_image.jpg", b"file_content", content_type="image/jpeg"),
        }
        form = SubmitBugsForm(data=form_data, files=form_data)
        self.assertEqual(form.errors['description'], ['This field is required.'])

    def test_missing_image_type(self):
        form_data = {
            'title': 'Test Bug Title',
            'description': 'Test Bug Description',
        }
        form = SubmitBugsForm(data=form_data, files=form_data)
        self.assertEqual(form.errors['image'], ['This field is required.'])

    def test_blank_form_submission(self):
        form_data = {}
        form = SubmitBugsForm(data=form_data, files=form_data)
        self.assertEqual(form.errors['title'], ['This field is required.'])
        self.assertEqual(form.errors['description'], ['This field is required.'])
        self.assertEqual(form.errors['image'], ['This field is required.'])

    def test_form_incorrect_info(self):
        form_data = {
            'title': 85,
            'description': -1,
            'image': 0
        }
        form = SubmitBugsForm(data=form_data, files=form_data)
        self.assertFalse(form.is_valid())

    def test_form_blank_not_valid(self):
        form_data = {}
        form = SubmitBugsForm(data=form_data, files=form_data)
        self.assertFalse(form.is_valid())
