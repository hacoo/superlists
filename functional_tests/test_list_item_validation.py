from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):


    def test_cannot_add_empty_list_items(self):
        # Edith accidentally enters a blank list item.
        # She hits enter on an empty list box:
        self.browser.get(self.server_url)
        # The home page refreshes and given an error saying
        # that blank input is not valid.
        
        self.browser.find_element_by_id('id_new_item').send_keys('\n')
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")

        # She tries again (with input).
        self.browser.find_element_by_id('id_new_item').send_keys("Buy milk\n")
        
        # It works.
        self.check_for_row_in_list_table("1: Buy milk")

        # Perversely, she then tries another blank line:
        self.browser.find_element_by_id('id_new_item').send_keys('\n')

        # It still gives an error message.
        self.check_for_row_in_list_table("1: Buy milk")
        error = self.browser.find_element_by_css_selector('.has-error')
        self.assertEqual(error.text, "You can't have an empty list item")
        
        # She can correct it, add some text, which will be recorded:
        self.browser.find_element_by_id('id_new_item').send_keys("Make tea\n")
        self.check_for_row_in_list_table("1: Buy milk")
        self.check_for_row_in_list_table("2: Make tea")

        
