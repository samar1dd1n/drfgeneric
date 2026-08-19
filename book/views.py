from django.shortcuts import render
from rest_framework import status , generics
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import NotFound
from rest_framework.generics import get_object_or_404
from .models import Book
from .serializers import BookSerializer
from rest_framework.viewsets import ViewSet


class BookCRUD(ViewSet):
    def list(self, request):
        book = Book.objects.all()
        serializer = BookSerializer(book, many=True)
        return Response(
            {
                'msg' : 'Book List',
                'count' : len(book),
                'books' : serializer.data

            },
            status = status.HTTP_200_OK
        )
    def create(self, request):
        serializer = BookSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {
                'msg' : 'Book Created',
                'Book' : serializer.data
            },
            status = status.HTTP_201_CREATED
        )
    def retrieve(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        serializer = BookSerializer(book)

        return Response(
            {
                'msg' : 'Book details',
                'Book' : serializer.data
            },
            status = status.HTTP_200_OK
        )
    def update(self, request, pk):
        serializer = BookSerializer(instance=get_object_or_404(Book,pk = pk), data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'msg' : 'Book Updated',
            'Book' : serializer.data
        },status=status.HTTP_200_OK)
    def partial_update(self, request, pk):
        serializer = BookSerializer(instance=get_object_or_404(Book,pk =pk), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            'msg' : 'Book Updated',
            'Book' : serializer.data
        },status=status.HTTP_200_OK)

    def destroy(self, request, pk):
        book = get_object_or_404(Book, pk=pk)
        book.delete()
        return Response({
            'msg' : 'Book Deleted',
        },status=status.HTTP_204_NO_CONTENT)
