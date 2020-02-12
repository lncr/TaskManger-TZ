from django.test import TestCase

from .models import Task, Tag


class TaskModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Task.objects.create(name='test',
                            description='asdfghjkl')

    def test_name_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_description_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('description').verbose_name
        self.assertEquals(field_label, 'description')

    def test_date_label(self):
        task = Task.objects.get(id=1)
        field_label = task._meta.get_field('date_of_creation').verbose_name
        self.assertEquals(field_label, 'date of creation')


class TagModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Tag.objects.create(name='test')

    def test_name_label(self):
        tag = Tag.objects.get(id=1)
        field_label = tag._meta.get_field('name').verbose_name
        self.assertEquals(field_label, 'name')

    def test_date_label(self):
        tag = Tag.objects.get(id=1)
        field_label = tag._meta.get_field('date_of_creation').verbose_name
        self.assertEquals(field_label, 'date of creation')
