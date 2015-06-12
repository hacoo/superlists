from django.test import TestCase # testcase is an augmented version of unittest.
from django.core.urlresolvers import resolve
from django.http import HttpRequest

from lists.views import home_page


# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        
        found = resolve('/')
        self.assertEquals(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # Test if the HTML returned by the home_page view has some basic properties
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title> To-Do lists </title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))
        