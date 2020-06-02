from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from blog.views import post_list  

class HomePageTest(TestCase):

    def test_root_url_resolves_to_post_list_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, post_list)
    
    
    def test_post_list_returns_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'blog/post_list.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data= {'posts': posts})
        self.assertIn('A new post', response.content.decode())
        self.assertTemplateUsed(response, 'post_edit.html')
        