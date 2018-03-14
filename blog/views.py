from django.shortcuts import render
from django.http import HttpResponse


def main(request):
    return render(request, 'blog/index.html', locals())
