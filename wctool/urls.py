from django.urls import path
from . import views

urlpatterns = [
  path("all-files-names", views.get_all_files_names, name="get_all_files_names"),
  path("file-by-id", views.get_files_by_id, name="get_all_files_names"),
]
