 
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import unittest
import time
import sys

# A functional test story!
# Adapted from Harry J.W. Percival "Test Driven Development with Python "

class FunctionalTest(StaticLiveServerTestCase):

    #setUpClass is like the classmethod version of setUp -- it
    #only runs once, on class initialization, rather than once for
    #each object.
    @classmethod
    def setUpClass(cls):
        for arg in sys.argv:
            if 'liveserver' in arg:
                cls.server_url = 'http://' + arg.split('=')[1]
                return
        super().setUpClass()
        cls.server_url = cls.live_server_url

    @classmethod
    def tearDownClass(cls):
        if cls.server_url == cls.live_server_url:
            super().tearDownClass()

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    
    def tearDown(self):
        self.browser.quit()

    
    
    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows],
                      str("\n ERROR: To-do item " + row_text + " did not appear in the table. It's text was:"
                             + "\n " + table.text)
        )
        
        