from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_opens_blogs_home_page(self):  
        self.browser.get('http://localhost:8000')

        self.assertIn('Blog', self.browser.title) 

        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn('Blog', header_text)


        #self.fail('Finish the test!')  


if __name__ == '__main__':  
    unittest.main(warnings='ignore') 