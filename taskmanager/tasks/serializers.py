from rest_framework import serializers
from .models import Task, Tag


# serializer for reading tags, updating and deleting a tag
class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = ['id', 'name', 'date_of_creation', 'tasks']


# serializer for reading, updating and deleting a task
class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'date_of_creation', 'tags']


