from django.urls import path

from . import views


app_name = "documents"


urlpatterns = [

    path(
        "",
        views.document_list_view,
        name="list",
    ),

    path(
        "create/",
        views.document_create_view,
        name="create",
    ),

    path(
        "<int:pk>/",
        views.document_detail_view,
        name="detail",
    ),

    path(
        "<int:pk>/edit/",
        views.document_update_view,
        name="update",
    ),

    path(
        "<int:pk>/delete/",
        views.document_delete_view,
        name="delete",
    ),
    path(
        '<int:pk>/download/',
        views.document_download_view,
        name='download',
    ),

]