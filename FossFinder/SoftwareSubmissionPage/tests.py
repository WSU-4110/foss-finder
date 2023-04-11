from django.test import TestCase
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from SoftwareSubmissionPage.models import SubmittedSoftware
from django.utils import timezone
from django.urls import reverse
from SoftwareSubmissionPage.forms import SubmitSoftwareForm


class TestSoftwareSubmit(TestCase):
    def create_Software(self, name='name test', developer='dev test', description='desc test', tag_WordProcesser=True, tag_SpreadSheet=True, tag_GraphicsEditor=False, tag_AudioEditor=False, tag_Communication=False, tag_Multimedia=False, tag_AntiVirus=False, tag_CodeEditor=False, tag_DiskBurner=False, tag_FileShare=False, tag_Other=False, os_WIN=True, os_MAC=False, os_NIX=False, image="img/audacity.png"):
        return SubmittedSoftware.objects.create(name=name, developer=developer, description=description, tag_WordProcesser=tag_WordProcesser, tag_SpreadSheet=tag_SpreadSheet, tag_GraphicsEditor=tag_GraphicsEditor, tag_AudioEditor=tag_AudioEditor, tag_Communication=tag_Communication, tag_Multimedia=tag_Multimedia, tag_AntiVirus=tag_AntiVirus, tag_CodeEditor=tag_CodeEditor, tag_DiskBurner=tag_DiskBurner, tag_FileShare=tag_FileShare, tag_Other=tag_Other, os_WIN=os_WIN, os_MAC=os_MAC, os_NIX=os_NIX, image=image)
    
    def test_created_Software(self):
        x = self.create_Software()
        self.assertTrue(isinstance(x, SubmittedSoftware))
        self.assertEqual(x.__unicode__(), x.name)
    
    def test_form_valid(self):
        #x = SubmittedSoftware.objects.create(name='name test', developer='dev test', description='desc test', tag_WordProcesser=True, tag_SpreadSheet=True, tag_GraphicsEditor=False, tag_AudioEditor=False, tag_Communication=False, tag_Multimedia=False, tag_AntiVirus=False, tag_CodeEditor=False, tag_DiskBurner=False, tag_FileShare=False, tag_Other=False, os_WIN=True, os_MAC=False, os_NIX=False, image='img/audacity.png')
        x = self.create_Software()
        data = {'name': x.name, 'developer': x.developer, 'description': x.description, 'Word Processer': x.tag_WordProcesser, 
            'Spreadsheet Editor': x.tag_SpreadSheet, 'Graphics Editor': x.tag_GraphicsEditor, 'Audio Editor': x.tag_AudioEditor, 
            'Communication': x.tag_Communication, 'Multimedia': x.tag_Multimedia, 'AntiVirus': x.tag_AntiVirus, 'Code Editor': x.tag_CodeEditor, 
            'Disk Burner': x.tag_DiskBurner, 'File Sharing': x.tag_FileShare, 'Other': x.tag_Other, 'Windows': x.os_WIN, 
            'Mac OS X': x.os_MAC, 'Linux': x.os_NIX, 'image': x.image,}
        form = SubmitSoftwareForm(data=data)
        self.assertFalse(form.is_valid())

    def test_form_invalid(self):
        x = SubmittedSoftware.objects.create(name='name test', developer='dev test', description='desc test', tag_WordProcesser=True, tag_SpreadSheet=True, tag_GraphicsEditor=False, tag_AudioEditor=False, tag_Communication=False, tag_Multimedia=False, tag_AntiVirus=False, tag_CodeEditor=False, tag_DiskBurner=False, tag_FileShare=False, tag_Other=False, os_WIN=True, os_MAC=False, os_NIX=False, image="img/audacity.png")
        data = {'name': x.name, 'developer': x.developer, 'description': x.description, 'Word Processer': x.tag_WordProcesser, 
            'Spreadsheet Editor': x.tag_SpreadSheet, 'Graphics Editor': x.tag_GraphicsEditor, 'Audio Editor': x.tag_AudioEditor, 
            'Communication': x.tag_Communication, 'Multimedia': x.tag_Multimedia, 'AntiVirus': x.tag_AntiVirus, 'Code Editor': x.tag_CodeEditor, 
            'Disk Burner': x.tag_DiskBurner, 'File Sharing': x.tag_FileShare, 'Other': x.tag_Other, 'Windows': x.os_WIN, 
            'Mac OS X': x.os_MAC, 'Linux': x.os_NIX, 'image': x.image,}
        form = SubmitSoftwareForm(data=data)
        self.assertFalse(form.is_valid())


class TestView(unittest.TestCase): 
    def test_software_submit_button(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8000/SoftwareSubmissionPage")
        #self.driver.find_element(By.XPATH, "//*[@id='id_name']").send_keys("test name")
        #self.driver.find_element(By.NAME, 'id_name').send_keys("test name")
        self.driver.find_element(By.XPATH, '//*[@id="id_tag_WordProcesser"]').click()
        self.assertIn("http://localhost:8000/", self.driver.current_url)
        self.driver.quit()

    def test_software_submit_tags_valid(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8000/SoftwareSubmissionPage")
        self.driver.find_element(By.XPATH, '//*[@id="id_tag_WordProcesser"]').click()
        self.assertIn("http://localhost:8000/", self.driver.current_url)
        self.driver.quit()

    def test_software_submit_tags_invalid(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://localhost:8000/SoftwareSubmissionPage")
        self.driver.find_element(By.XPATH, '//*[@id="id_tag_WordProcesser"]').send_keys("words")
        self.assertIn("http://localhost:8000/", self.driver.current_url)
        self.driver.quit()

    if __name__ == '__main__':
        unittest.main()