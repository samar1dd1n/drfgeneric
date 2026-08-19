from django.db.migrations import serializer
from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from rest_framework.exceptions import NotFound
from rest_framework.generics import get_object_or_404, RetrieveUpdateDestroyAPIView
from car.models import Car
from car.serializers import CarSerializer
from rest_framework.generics import GenericAPIView

class CarListCreateView(GenericAPIView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer

    def get(self,request):
        serializer = self.get_serializer(self.get_queryset(),many = True)
        return Response(
            {
                'msg': 'Book List',
                'count': len(self.get_queryset()),
                'books': serializer.data

            },
            status=status.HTTP_200_OK
        )
    def post(self,request):
        serializer = self.get_serializer(self.queryset() ,many = True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'msg': 'Book Created',
                'Book': serializer.data
            },
            status=status.HTTP_201_CREATED
        )


class CarRetrieveUpdateDestroyView(GenericAPIView):
    serializer_class = CarSerializer

    def get_object(self,pk):
        return get_object_or_404(Car,pk=pk)

    def get(self ,request, pk):
        serializer = self.get_serializer(self.get_object(pk))

        return Response(
            {
                'msg': 'Book details',
                'Book': serializer.data
            },
            status=status.HTTP_200_OK
        )

    def put(self,request,pk):
        serializer = self.get_serializer(instance =self.get_object(pk),data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()


        return Response({
            'msg': 'Book Updated',
            'Book': serializer.data
        }, status=status.HTTP_200_OK)


    def patch(self, request, pk):
        serializer = self.get_serializer(instance=self.get_object(pk), data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'msg': 'Book Updated',
            'Book': serializer.data
        }, status=status.HTTP_200_OK)


    def destroy(self, request, pk):
        book = get_object_or_404(Car, pk=pk)
        book.delete()
        return Response({
        'msg' : 'Book Deleted',
        },status=status.HTTP_204_NO_CONTENT)

