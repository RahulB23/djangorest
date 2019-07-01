from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpRequest
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from lib.models import User, Book
from lib.serializers import UserSer, BookSer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import status


# Create your views here.


@csrf_exempt
def user_list(request):

    #list all users
    if request.method == 'GET':
        user = User.objects.all()
        serializer = UserSer(user, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def books_list(request):

    #list all books
    if request.method == 'GET':
        book = Book.objects.all()
        serializer = BookSer(book, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = BookSer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


def user_detail(request, pk):

    try:
        user = User.objects.get(pk=pk)
    except User.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = UserSer(user)
        return JsonResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = UserSer(user, data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        user.delete()
        return HttpResponse(status=204)


def book_detail(request, pk):

        try:
            book = Book.objects.get(pk=pk)
        except Book.DoesNotExist:
            return HttpResponse(status=404)

        if request.method == 'GET':
            serializer = BookSer(book)
            return JsonResponse(serializer.data)

        elif request.method == 'PUT':
            data = JSONParser().parse(request)
            serializer = BookSer(book, data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data)
            return JsonResponse(serializer.errors, status=400)

        elif request.method == 'DELETE':
            book.delete()
            return HttpResponse(status=204)



def Reg_user(request):
        username = request.data.get("username")
        password = request.data.get("password")


        new_user = User.objects.create_user(
            user_name=username, user_pass=password
        )
