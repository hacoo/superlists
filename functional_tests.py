from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest
import time

# A functional test story!
# Adapted from Harry J.W. Percival "Test Driven Development with Python "

class NewVisitorTest(unittest.TestCase):

    # setUp is always run at the beginning
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)
        
    # tearDown is always run at the end (even if error)
    def tearDown(self):
        self.browser.quit()

    # Any function starting with test will be ru
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Annie is trying out a cool new online to-do list app.
        # She goes to the homepage:
        self.browser.get('http://localhost:8000')
        
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

        
        
        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(
            '1: Buy peacock feathers', [row.text for row in rows],
            "\n ERROR: New to-do item did not appear in table -- it's text was: \n%s" % (table.text)
            )
        
        
        # There is still a test box to add an item. She enteres
        # "Use peacock feathers to make a fly"
        inputbox = self.browser.find_element_by_id('id_new_item')
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertIn(
            '1: Buy peacock feathers', [row.text for row in rows],
            "\n ERROR: To-Do item 1 did not appear in table -- it's text was: \n%s" % (table.text)
            )
        self.assertIn(
            '2: Use peacock feathers to make fly', [row.text for row in rows],
            "\n ERROR: To-Do item 2 did not appear in table -- it's text was: \n%s" % (table.text)
            )


        

        # The page updates again, and now shows both items in the list

        # Annie wonders if the page will remember her list. She
        # sees that the site has generated a unique URL for her.
        # There's some explanatory text.

        # She visits the URL - her todo list is still there!

        # She quits the browser in satisfaction.

        self.fail('test is not complete yet!') # Test will always fail (since it's not yet done)
        
    # this checks to see if this script is being run from the command line
    # (not another script.) So it will immediately run the testrunner
if __name__ == '__main__':
    unittest.main()




