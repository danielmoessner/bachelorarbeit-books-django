from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render
import requests

class BooksView(APIView):
    def get(self, *args, **kwargs):
        sales = requests.get('http://localhost:8230/')
        sales = sales.json()
        books = [
            {
                'id': 1,
                "name": "1984",
                "author": "George Orwell",
                "published": 1949
            },
            {
                'id': 2,
                "name": "The Gulag Archipelago",
                "author": "Aleksandr Solzhenitsyn",
                "published": 2018
            }
        ]
        for book in books:
            book['sales'] = len(list(filter(lambda item: item['book'] == book['id'], sales)))
        return Response(books)
