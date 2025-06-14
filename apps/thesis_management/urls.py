from django.urls import path
from . import views
from .files_processor.extract_data import request_thesis_data

urlpatterns = [
    path("process_file/", request_thesis_data, name="request_thesis_data"),
    path("upload_thesis/", views.crear_tesis_view, name="upload_thesis"),
    path("upload_career/", views.upload_career, name="upload_career"),
]

