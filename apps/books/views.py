from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render


class BooksView(APIView):
    def get(self, *args, **kwargs):
        books = [
            {
                "name": "1984",
                "author": "George Orwell",
                "published": 1949
            },
            {
                "name": "The Gulag Archipelago",
                "author": "Aleksandr Solzhenitsyn",
                "published": 2018
            }
        ]
        return Response(books)
