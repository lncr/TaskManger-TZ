from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Tag, Task


class TaskTests(APITestCase):

    def setUp(self):
        Task.objects.create(name='Run marathon', description='Need to run a marathon')
        Task.objects.create(name='Lie on the beach', description='Need some more sunlight')

    def test_create_task(self):
        url = reverse('tasks_list_url')
        data = {'name': 'Buy milk', 'description': 'Need some milk'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.get().name, 'Buy milk')

    def test_get_single_task(self):
        url = reverse('task_detail_url', args=2)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_tasks_list(self):
        url = reverse('tasks_list_url')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class TagTests(APITestCase):

    def setUp(self):
        Tag.objects.create(name='marathon')

    def test_create_tag(self):
        url = reverse('tags_list_url')
        data = {'name': 'milk'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Tag.objects.get().name, 'milk')

    def test_get_single_tag(self):
        url = reverse('tag_detail_url', args=1)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_tags_list(self):
        url = reverse('tags_list_url')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
