from django.test import TestCase
from .forms import ItemForm

class TestItemForm(TestCase):

    def test_item_name_is_required(self): #test that item name is mandatory
        form = ItemForm({'name': ''}) #try to create item with empty string
        self.assertFalse(form.is_valid()) #checks if  form is valid, which it is not due empty string
        self.assertIn('name', form.errors.keys()) #making sure that error occured in the form
        self.assertEqual(form.errors['name'][0], u'This field is required.') #checking that correct error message received

    
    def test_done_not_required(self):
        form = ItemForm({'name': 'test to do item form'})
        self.assertTrue(form.is_valid())


    def test_fields_are_explicit_in_form_meta_class(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done']) #ensuring that only fields from models.py MetaClass are there