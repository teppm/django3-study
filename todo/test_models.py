from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_default_is_false(self): #testing that all items created are with done status set to false i.e not done
        item = Item.objects.create(name='test todo , done=false') #create a item with name 
        self.assertFalse(item.done) #tests that item.done is false, i.e item not done when created

    
    def test_item_string_method_returns_name(self): #testing that item returns a name 
        item = Item.objects.create(name='test todo')
        self.assertEqual(str(item), 'test todo') #checks this name is returned when we render this item as string
        

