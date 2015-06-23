from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):


    def test_cannot_add_empty_list_items(self):
        # Edith accidentally enters a blank list item.
        # She hits enter on an empty list box:
        self.browser.get(self.server_url)
        # The home page refreshes and given an error saying
        # that blank input is not valid.
        
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # She tries again (with input).
        self.get_item_input_box().send_keys("Buy milk\n")
        
        # It works.
        self.check_for_row_in_list_table("1: Buy milk")

        # Perversely, she then tries another blank line:
        self.get_item_input_box().send_keys('\n')

        # It still gives an error message.
        self.check_for_row_in_list_table("1: Buy milk")
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")
        
        # She can correct it, add some text, which will be recorded:
        self.get_item_input_box().send_keys("Make tea\n")
        self.check_for_row_in_list_table("1: Buy milk")
        self.check_for_row_in_list_table("2: Make tea")

    
    def test_cannot_add_duplicate_list_items(self):
        # Edith starts a new list from the home page:
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1: Buy wellies')

        # Then she tries to enter a duplicate item. Drama!
        self.get_item_input_box().send_keys('Buy wellies\n')

        # Fortunately, she sees a helpful error message:
        self.check_for_row_in_list_table('1: Buy wellies')
        error = self.get_error_element()
        self.assertEqual(error.text, "You've already got this item in your list")

    def test_error_messages_are_cleared_on_input(self):
        # Edith start a new list in a way that causes a validation error:
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())

        # She starts typing in the box. The error is cleared!
        self.get_item_input_box().send_keys('a')

        # The message is gone!
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')