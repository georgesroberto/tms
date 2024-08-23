from django.test import TestCase
from django.urls import reverse
from django.utils import timezone
from .models import Task ,Author, Tag

# Create your tests here.

# class TaskCreateViewTests(TestCase):
#     def setUp(self) -> None:
#         self.author = Author.objects.create(name='Clinton')
#         self.tag = Tag.objects.create(name='MyTag')
        

#     def test_with_valid_data(self):
#         response = self.client.post(reverse('add'), {
#             'title': 'New Task',
#             'description': 'My Description',
#             'status': 'due',
#             'due_date': timezone.now().date(),
#             'avator': 'a.png',
#             'author': self.author,
#             'tag': self.tag,
#         })

#         self.assertEqual(response.status_code, 302)
#         # self.assertEqual(Task.objects.all(), 0)
#         self.assertEqual(Task.objects.first().title, 'New Task')

       
#     def tearDown(self) -> None:
#         self.author.delete()
#         self.tag.delete()

#         return super().tearDown()

class TestAuotherModel(TestCase):
    def test_str_author(self):
        author = Author.objects.create(name='Joe')
        self.assertEqual(str(author), 'Joe')