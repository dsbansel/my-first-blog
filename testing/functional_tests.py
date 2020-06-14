from selenium import webdriver
import time
import unittest

class NewVisitorTest(unittest.TestCase):  

    def setUp(self):  
        self.browser = webdriver.Firefox()

    def tearDown(self):  
        self.browser.quit()

    def test_opens_blog_home_page_and_browses(self):  
        #user opens blog home page
        self.browser.get('http://dsb874.pythonanywhere.com/')

        #they expect the correct header and title to be shown
        self.assertIn("Davinder's Blog", self.browser.title) 
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn("Davinder's Blog", header_text)    

        #they then move on to the CV page
        self.opens_CV_page()

        #this also needs the correct header and title
        self.assertIn("Davinder's CV", self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text  
        self.assertIn("Davinder's CV", header_text)

        #they also see an option to return to the Blog site
        header_text = self.browser.find_element_by_tag_name('h3').text  
        self.assertIn("Davinder's Blog", header_text)

        #they test this link
        self.browser.get('http://dsb874.pythonanywhere.com/')

        #they then move back to the CV page
        self.opens_CV_page()

        #they click on a section of the CV expect to see the details
        self.browser.get('http://dsb874.pythonanywhere.com/section/1/')

        #they click edit and expect to see the option to edit the section
        self.browser.get('http://dsb874.pythonanywhere.com/section/1/edit/')

        #they then move back to the CV page
        self.opens_CV_page()

        #they click on another section of the CV expect to see the details
        self.browser.get('http://dsb874.pythonanywhere.com/section/2/')

        #they click edit and expect to see the option to edit the section
        self.browser.get('http://dsb874.pythonanywhere.com/section/2/edit/')

        time.sleep(3)



    def opens_CV_page(self):
        self.browser.get('http://dsb874.pythonanywhere.com/CV')

# def test_opens_CV_section_detail(self):
# def test_opens_CV_section_edit(self):

if __name__ == '__main__':  
    unittest.main(warnings='ignore') 