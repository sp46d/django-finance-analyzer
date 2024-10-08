from django.urls import path
from . import views

app_name = "budget"
urlpatterns = [
    path("", views.home_page, name="home"),
    path("new/", views.new_transaction, name="new"),
    path("upload/", views.upload_file, name="upload"),
]
