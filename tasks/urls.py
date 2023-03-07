from django.urls import path
from tasks.views import create_task, show_mine

urlpatterns = [
    path("create/", create_task, name="create_task"),
    path("mine/", show_mine, name="show_my_tasks"),
]
