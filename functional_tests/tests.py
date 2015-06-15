
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
#import unittest
import time

# A functional test story!
# Adapted from Harry J.W. Percival "Test Driven Development with Python "

class NewVisitorTest(StaticLiveServerTestCase):

    # setUp is always run at the beginning
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    # tearDown is always run at the end (even if error)
    def tearDown(self):
        self.browser.quit()

    def check_for_row_in_list_table(self, row_text):
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(row_text, [row.text for row in rows],
                      str("\n ERROR: To-do item " + row_text + " did not appear in the table. It's text was:"
                             + "\n " + table.text)
        )
        
    def test_layout_and_styling(self):
        # Edith goes to the home page.
        self.browser.get(self.live_server_url)
        self.browser.set_window_size(1024, 768)

        # It's got a beutiful ceneter input box!
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta = 5, 
        )

        # Edith starts a new test - the box is still centered.
        inputbox.send_keys('testing \n')
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta = 5, 
        )


        
    def SUPPRESS_test_can_start_a_list_and_retrieve_it_later(self):
        """ Run a basic functional test showing that a list can
        be created and retrieved. """
        # Edith is trying out a cool new online to-do list app.
        # She goes to the homepage:
        self.browser.get(self.live_server_url)
        
        # She notices the header and title mention to-do lists:
        self.assertIn('To-Do', self.browser.title)        
        header_test = self.browser.find_element_by_tag_name('h1').text

        
        
        # She's immediately invited to enter a to-do item.
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
                inputbox.get_attribute('placeholder'),
                'Enter a to-do item'
            )
        
        # She's into making fishing flies, so she types in
        # "Buy peacock feathers"
        inputbox.send_keys('Buy peacock feathers')

        # When she hits enters, the page updates, containing
        # the item she entered as so:
        # 1. "Buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        
        # There is still a test box to add an item. She enteres
        # "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)
        
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')

        

        # The page updates again, and now shows both items in the list

        # Edith wonders if the page will remember her list. She
        # sees that the site has generated a unique URL for her.
        # There's some explanatory text.

        # She visits the URL - her todo list is still there!

        # She quits the browser in satisfaction.
        self.browser.quit()

        # A new user, Francis, goes to the site.
        ## Frances starts a new browser
        self.browser = webdriver.Firefox()
        self.browser.get(self.live_server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)

        # Francis starts entering a new list. He's kind of boring.
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Buy milk')
        inputbox.send_keys(Keys.ENTER)

        # Francis gets his own URL.
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url,'/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url)

        # Still no trace of Edith's list, but the new item is there
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly', page_text)
        self.assertIn('Buy milk', page_text)

        # Fracis leaves in joy.

        self.fail('test is not complete yet!') # Test will always fail (since it's not yet done)
        
    # this checks to see if this script is being run from the command line
    # (not another script.) So it will immediately run the testrunner
#if __name__ == '__main__':
 #   unittest.main()













        
        