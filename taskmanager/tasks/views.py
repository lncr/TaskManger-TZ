from rest_framework import viewsets

from .models import Task, Tag
from .serializers import TaskSerializer, TagSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    lookup_field = 'id'
    queryset = Task.objects.all()


class TagViewSet(viewsets.ModelViewSet):
    serializer_class = TagSerializer
    lookup_field = 'id'
    queryset = Tag.objects.all()
