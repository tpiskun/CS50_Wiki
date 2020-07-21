from django.urls import path

from . import views

app_name = "encyclopedia"
urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:page>", views.page, name="page"),
    path("wiki/<str:entry>", views.Convert_Entry, name="convert_entry"),
    path("edit/<str:edit_page>", views.Edit_Page, name="edit_page"),
    path("search", views.Search, name="search"),
    path("new_page", views.New_Page, name="new_page"),
    path("random_page", views.Random_Page, name="random_page"),
]
