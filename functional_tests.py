from selenium import webdriver
import unittest


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

    # Any function starting with test will be run
    def test_can_start_a_list_and_retrieve_it_later(self):
        # Annie is trying out a cool new online to-do list app.
        # She goes to the homepage:
        self.browser.get('http://localhost:8000')

        # She notices the header and title mention to-do lists:
        self.assertIn('To-Do', self.browser.title)        
        self.fail('test is not complete yet!') # Test will always fail (since it's not yet done)

        # She's immediately invited to enter a to-do item.

        # She's into making fishing flies, so she types in
        # "buy peacock feathers"

        # When she hits enters, the page updates, containing
        # the item she entered as so:
        # 1. "Buy peacock feathers"

        # There is still a test box to add an item. She enteres
        # "Use peacock feathers to make a fly"

        # The page updates again, and now shows both items in the list

        # Annie wonders if the page will remember her list. She
        # sees that the site has generated a unique URL for her.
        # There's some explanatory text.

        # She visits the URL - her todo list is still there!

        # She quits the browser in satisfaction.

    # this checks to see if this script is being run from the command line
    # (not another script.) So it will immediately run the testrunner
if __name__ == '__main__':
    unittest.main()




