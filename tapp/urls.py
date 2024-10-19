from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDeleteView, TaskListApiView, TaskListByApi

# Route
urlpatterns = [
    path('', TaskList.as_view(), name='list'),
    path('add/', TaskCreate.as_view(), name='add'),
    path('detail/<int:pk>/', TaskDetail.as_view(), name='detail'),
    path('update/<int:pk>/', TaskUpdate.as_view(), name='update'),
    path('delete/<int:pk>', TaskDeleteView.as_view(), name='delete'),

    path('api/tasks/', TaskListApiView.as_view(), name='api'),
    path('api-list/', TaskListByApi.as_view(), name='api-list'),
]