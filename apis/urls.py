from django.urls import path
from .views import AuthorAPIView, AuthorDetailsAPIView, BookAPIView, BookDetailsAPIView


urlpatterns = [
    path(
        "authors/",
        AuthorAPIView.as_view(),
        name="Authors"
    ),
    path(
        "authors/<int:author_id>/",
        AuthorDetailsAPIView.as_view(),
        name="AuthorDetails"
    ),

    path(
        "books/",
        BookAPIView.as_view(),
        name="Books"
    ),
    path(
        "books/<int:book_id>/",
        BookDetailsAPIView.as_view(),
        name="BookDetails"
    ),
]
