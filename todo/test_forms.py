from django.test import TestCase
from .forms import ItemForm

class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        form = ItemForm({'name': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        self.assertEqual(form.errors['name'][0], u'This field is required.')

    
    def test_done_not_required(self):
        form = ItemForm({'name': 'test to do item form'})
        self.assertTrue(form.is_valid())


    def test_fields_are_explicit_in_form_meta_class(self):
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])