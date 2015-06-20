from django.test import TestCase # testcase is an augmented version of unittest.
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from django.utils.html import escape

from lists.views import home_page
from lists.models import Item, List


# Create your tests here.

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        
        found = resolve('/')
        self.assertEquals(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        # Test if the HTML returned by the home_page view has some basic properties
        request = HttpRequest()
        expected_html = render_to_string('home.html')
        
        response = home_page(request)

        self.assertEqual(response.content.decode(), expected_html)


    def test_home_page_only_saves_items_when_necessary(self):
        request = HttpRequest()
        home_page(request)
        self.assertEqual(Item.objects.count(), 0)
        
        
class ListViewTest(TestCase):

    def test_home_page_displays_this_list_items_only(self):
        correct_list = List.objects.create()
        Item.objects.create(text='itemey 1', list=correct_list)
        Item.objects.create(text='itemey 2', list=correct_list)        
        other_list = List.objects.create()
        Item.objects.create(text='other item 1', list=other_list)
        Item.objects.create(text='other item 2', list=other_list)

        response = self.client.get('/lists/%d/' % (correct_list.id))

        self.assertContains(response, 'itemey 2')
        self.assertContains(response, 'itemey 1')
        self.assertNotContains(response, 'other item 1')
        self.assertNotContains(response, 'other item 2')

        
    def test_passes_correct_list_to_templat(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()
        response = self.client.get('/lists/%d/' % (correct_list.id))
        self.assertEqual(response.context['list'], correct_list)
    
    def can_save_multiple_POST_request_to_existing_list(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        self.client.post(
            '/lists/%d/' % (correct_list.id),
            data = {'item_text': 'A new item for existing list'}
        )

        self.client.post(
            '/lists/%d/' % (correct_list.id),
            data = {'item_text': 'A second item for existing list'}
        )


        self.assertEqual(Item.objects.count, 1)
        new_item = Item.objects.first()
        second_item = Item.objects.second()
        self.assertEqual(new_item.text, 'A new item for exiting list')
        self.assertEqual(second_item.text, 'A second item for exiting list')
        self.assertEqual(new_item.list, correct_list)
        self.assertEqual(second_item.list, correct_list)


    def test_POST_redirects_to_list_view(self):
        other_list = List.objects.create()
        correct_list = List.objects.create()

        response = self.client.post(
            '/lists/%d/' % (correct_list.id),
            data = {'item_text': 'A new item for existing list'}
        )

        self.assertRedirects(response, '/lists/%d/' % (correct_list.id))

        
        
class NewListTest(TestCase):

    def test_validation_errors_are_sent_back_to_home_page_template(self):
        response = self.client.post('/lists/new', data={'item_text': ''})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response,'home.html')
        expected_error = escape("You can't have an empty list item")
        self.assertContains(response, expected_error)




        

            
        

        




    
    