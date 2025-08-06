from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from django.core.mail import send_mail
from drf_yasg.utils import swagger_auto_schema

from product.models import Author, Book
from product.serializers import AuthorSerializer, BookSerializer


class AuthorAPIView(APIView):
    def get(self, request):
        authors = Author.objects.all()
        serializer = AuthorSerializer(authors, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=AuthorSerializer)
    def post(self, request):
        data = request.data
        serializer = AuthorSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class BookAPIView(APIView):
    def get(self, request):
        books = Book.objects.all()

        query_params = request.query_params
        author_id = query_params.get("author_id")

        if author_id is not None:
            books = Book.objects.filter(author=author_id)

        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=BookSerializer)
    def post(self, request):
        data = request.data
        serializer = BookSerializer(data=data)

        if serializer.is_valid():
            product = serializer.save()
            
            send_mail(
                "New Book alert", 
                f"New book that named \"{product.name}\" is in the stores now!",
                "example@gmail.com",
                ["example@gmail.com"], # It works, i just changed my mail back to example
                fail_silently=False
            )

            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class AuthorDetailsAPIView(APIView):
    def get(self, request, author_id):
        author = get_object_or_404(Author, id=author_id)
        serializer = AuthorSerializer(author)
        return Response(serializer.data, status=status.HTTP_200_OK)


class BookDetailsAPIView(APIView):
    def get(self, request, book_id):
        book = get_object_or_404(Book, id=book_id)
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
