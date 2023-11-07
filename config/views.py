from django.http import HttpResponseNotFound, HttpResponseServerError
from django.shortcuts import render, redirect


def server_error(request):
    return HttpResponseServerError(
        '<h3>Ошибка 500: Ошибка сервера</h3>'
    )


def page_not_found(request, exception):
    return HttpResponseNotFound(
        '<h3>Ошибка 404: Такой страницы не существует</h3>'
    )
