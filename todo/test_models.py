from django.test import TestCase
from .models import Item

class TestModels(TestCase):
    
    def test_set_defaults_to_false(self):
        item = Item(name='Create test')
        item.save()
        self.assertEquals(item.name, "Create test")
        self.assertFalse(item.done, "False")
        
    def test_create_an_item_with_name_and_status(self):
        item = Item(name='Create test',done=True)
        item.save()
        self.assertEquals(item.name, "Create test")
        self.assertFalse(item.done, "True")
        
    def test_item_as_a_string(self):
        item = Item(name="Create test")
        self.assertEqual("Create test", str(item))