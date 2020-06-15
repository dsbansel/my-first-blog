from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.shortcuts import render, get_object_or_404

from CV.views import CV, section_detail, section_edit
from blog.views import post_list
from CV.models import Section


class CVPageTest(TestCase):

    def test_root_url_resolves_to_CV_view(self):
        found = resolve('/CV')  
        self.assertEqual(found.func, CV)

    def test_root_url_resolves_to_blog_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, post_list)
    
    def test_section_list_returns_correct_html(self):
        response = self.client.get('/CV')
        self.assertTemplateUsed(response, 'CV/CV_all_sections.html', 'CV/CV_base.html')

    def test_CV_url_resolves_to_section_detail_view(self):
        found = resolve('/section/1/')  
        self.assertEqual(found.func, section_detail)
 
    def test_section_detail_url_resolves_to_section_edit_view(self):
        found = resolve('/section/1/edit/')  
        self.assertEqual(found.func, section_edit)

    def test_correctly_save_and_read_from_database(self):
        #save new objects
        Section.objects.create(header='Personal Details')
        Section.objects.create(header='Education')
        Section.objects.create(header='Experience')

        response = self.client.get('/CV')

        #does the text that is read match the expected text?
        self.assertIn('Personal Details', response.content.decode())
        self.assertIn('Education', response.content.decode())
        self.assertIn('Experience', response.content.decode())
        
        #number of expected objects is equal to actual number of objects?
        saved_sections = Section.objects.all()
        self.assertEqual(saved_sections.count(), 3)


    def test_correctly_updates_database(self):
        #create 2 sections
        firstSection = Section()
        firstSection.header = 'Header 1'
        firstSection.text = 'text 1'
        firstSection.save()

        secondSection = Section()
        secondSection.header = 'Header 2'
        secondSection.text = 'text 2'
        secondSection.save()       

        #change the details
        firstSection.text = 'block of some text'
        firstSection.save()
        secondSection.header = 'Heading 2'
        secondSection.save()

        #save sections
        saved_sections = Section.objects.all()
        self.assertEqual(saved_sections.count(), 2)

        first_saved_item = saved_sections[0]
        second_saved_item = saved_sections[1]

        #does it recognise the changed or initial text?
        self.assertEqual(first_saved_item.text, 'block of some text')
        self.assertEqual(second_saved_item.header, 'Heading 2')