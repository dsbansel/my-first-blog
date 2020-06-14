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

    def test_correctly_read_from_database_on_homepage(self):
        Section.objects.create(header='Personal Details')
        Section.objects.create(header='Education')
        Section.objects.create(header='Experience')

        response = self.client.get('/CV')

        self.assertIn('Personal Details', response.content.decode())
        self.assertIn('Education', response.content.decode())
        self.assertIn('Experience', response.content.decode())


        
"""    
    def test_can_update_a_POST_request(self):
        response = self.client.post('/CV', data= {'sections': Section})
        self.assertIn('A new post', response.content.decode())
        self.assertTemplateUsed(response, 'section_edit.html')


    def test_section_edit_returns_correct_html(self):
        response = self.client.get('/section/1/edit/')
        self.assertTemplateUsed(response, 'CV/section_edit.html')

    def test_section_detail_returns_correct_html(self):
        response = self.client.get('/section/1/')
        self.assertTemplateUsed(response, 'CV/section_detail.html')
        """