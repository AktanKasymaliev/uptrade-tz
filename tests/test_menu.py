from django.test import TestCase
from django.urls import reverse

from menu.models import Notes

class TestMenu(TestCase):

    def setUp(self) -> None:
        self.note = Notes.objects.create(
            title="parent",
            content="parent"
        )
        self.note_child = Notes.objects.create(
            title="child",
            content="child",
            parent=self.note
        )

    def test_homepage(self):
        response = self.client.get("")
        self.assertTemplateUsed(response, 'home_page.html')
        
    def test_detailpage(self):
        response = self.client.get("/" + self.note.url + "/")
        self.assertTemplateUsed(response, 'detail_page.html')

    def test_parentness(self):
        childs_title = self.note.children.first().title
        parents_title = self.note.title
        self.assertEqual(childs_title, "child")
        self.assertEqual(parents_title, "parent")
