from django.test import TestCase
from .models import Item

# Create your tests here.

class TestViews(TestCase):


    def test_get_todo_list(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    
    def test_get_add_item_page(self):
        response = self.client.get('/add')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/add_item.html')
  

    def test_get_edit_item_page(self):  
        item = Item.objects.create(name='create to do item')
        response = self.client.get(f'/edit/{item.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')


    def test_can_add_item(self):
        response = self.client.post('/add', {'name': 'testing items'})
        self.assertRedirects(response, '/')


    def test_can_delete_item(self):
        item = Item.objects.create(name='create to do item') #create objects
        response = self.client.get(f'/delete/{item.id}') #delete objects
        self.assertRedirects(response, '/') #ensure correct redirect matches views.py redirect
        existing_items = Item.objects.filter(id=item.id) #search for deleted items
        self.assertEqual(len(existing_items), 0) #verify if length of items is 0 as all are deleted

    def test_can_toggle_item(self):
        item = Item.objects.create(name='create to do item', done=True) #create object with done status True
        response = self.client.get(f'/toggle/{item.id}') #toggle function for created object
        self.assertRedirects(response, '/') #ensure correct redirect matches views.py redirect
        updated_item = Item.objects.get(id=item.id) #get the updated item that is now done=False
        self.assertFalse(updated_item.done) #ensure that false that item is done , check previous


    def test_can_edit_item(self):
        item = Item.objects.create(name='create to do item') #create new item to work with in this test
        response = self.client.post(f'/edit/{item.id}', {'name': 'new update todo item'}) #get the above created item and post a changed name 
        updated_item = Item.objects.get(id=item.id) #get updated item
        self.assertEqual(updated_item.name, 'new update todo item') #check that update item name equals string
        