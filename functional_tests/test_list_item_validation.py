from unittest import skip
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):


    def test_cannot_add_empty_list_items(self):
        # Edith accidentally enters a blank list item.
        # She hits enter on an empty list box:

        # The home page refreshes and given an error saying
        # that blank input is not valid.

        # She tries again (with input).

        # It works.

        # Perversely, she then tries another blank line:

        # It still gives an error message.

        # She can correct it, add some text, which will be recorded:

        self.fail('write me!')

        
