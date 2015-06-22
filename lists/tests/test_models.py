from lists.models import Item, List
from django.test import TestCase
from django.core.exceptions import ValidationError

class ListAndItemModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        list_ = List()
        list_.save()
        
        first_item = Item()
        first_item.text = 'The first ever list item'
        first_item.list = list_
        first_item.save()

        second_item = Item()
        second_item.text = 'The second item'
        second_item.list = list_
        second_item.save()

        saved_list = List.objects.first()
        self.assertEqual(saved_list, list_)

        saved_items = Item.objects.all() # This returns a QuerySet object
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first ever list item')
        self.assertEqual(second_saved_item.text, 'The second item')
        self.assertEqual(first_saved_item.list, list_)
        self.assertEqual(second_saved_item.list, list_)


    def test_cannot_save_empty_list(self):
        list_ = List.objects.create()
        item = Item(list=list_, text='')
        with self.assertRaises(ValidationError):
            item.save()
            item.full_clean()

    def test_blank_items_are_not_saved(self):
        self.client.post('/lists/new', data={"text": ''})
        self.assertEqual(List.objects.count(), 0)
        self.assertEqual(Item.objects.count(), 0)

    def test_get_absolute_url(self):
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(), '/lists/%d/' % (list_.id))

    def test_duplicate_items_are_not_valid(self):
        list_ = List.objects.create()
        Item.objects.create(list=list_, text='bla')
        with self.assertRaises(ValidationError):
            item = Item(list=list_, text='bla')
            item.full_clean()
            #item.save()

    def test_CAN_save_item_to_different_lists(self):
        list1 = List.objects.create()
        list2 = List.objects.create()
        Item.objects.create(list = list1, text = 'bla')
        item = Item(list = list2, text = 'bla')
        item.full_clean() # Should not raise a ValidationError

    
        