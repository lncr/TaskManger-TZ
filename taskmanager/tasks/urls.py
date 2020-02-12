from django.urls import path

from .views import TaskViewSet, TagViewSet

urlpatterns = [
    path('tasks/', TaskViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('tasks/<int:id>/', TaskViewSet.as_view({'get': 'retrieve', 'delete': 'destroy',
                                                 'put': 'update', 'patch': 'partial_update'})),
    path('tags/', TagViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('tags/<int:id>/', TagViewSet.as_view({'get': 'retrieve', 'delete': 'destroy',
                                               'put': 'update', 'patch': 'partial_update'})),

]
