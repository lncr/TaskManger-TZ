from django.urls import path

from .views import TaskViewSet, TagViewSet

urlpatterns = [
    path('tasks/', TaskViewSet.as_view({'get': 'list', 'post': 'create'}), name='tasks_list_url'),
    path('tasks/<int:id>/', TaskViewSet.as_view({'get': 'retrieve', 'delete': 'destroy',
                                                 'put': 'update', 'patch': 'partial_update'}), name='task_detail_url'),
    path('tags/', TagViewSet.as_view({'get': 'list', 'post': 'create'}), name='tag_list_url'),
    path('tags/<int:id>/', TagViewSet.as_view({'get': 'retrieve', 'delete': 'destroy',
                                               'put': 'update', 'patch': 'partial_update'}), name='tag_detail_url'),

]
