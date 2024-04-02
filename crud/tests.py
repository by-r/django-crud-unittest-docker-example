from django.test import TestCase
from .models import Todolist
# Create your tests here.

class TodoTestCase(TestCase):
    @classmethod
    def setUpTestData(cls) -> None:
        return super().setUpTestData()
    
    def testTodo(self):
        todo = Todolist(title='test', desc='test', isdone=False)
        self.assertEqual(todo.title, 'test')
        self.assertEqual(todo.desc, 'test')
        self.assertEqual(todo.isdone, False)
        
    def testHomeURL(self):
        response = self.client.get("/todos/")
        self.assertEqual(response.status_code, 200)
    
    def testCreateURL(self):
        response = self.client.get("/todos/create/")
        self.assertEqual(response.status_code, 200)
        