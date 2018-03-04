from django.http import HttpResponse
from .models import Article
from django.core.exceptions import ObjectDoesNotExist


def index(_):
    return HttpResponse("Hello from mike")


def get(_, id):
    try:
        article = Article.objects.get(pk=id)
        return article
    except ObjectDoesNotExist:
        return HttpResponse("404")
