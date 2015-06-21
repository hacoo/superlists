from unittest import skip
from .base import FunctionalTest

class LayoutAndStylingTest(FunctionalTest):

    @skip
    def test_layout_and_styling(self):
        # Edith goes to the home page.
        self.browser.get(self.server_url)
        self.browser.set_window_size(1024, 768)

        # It's got a beutiful ceneter input box!
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta = 5, 
        )

        # Edith starts a new test - the box is still centered.
        inputbox.send_keys('testing \n')
        inputbox = self.get_item_input_box()
        self.assertAlmostEqual(
            inputbox.location['x'] + inputbox.size['width'] / 2,
            512,
            delta = 5, 
        )


