from django.shortcuts import render


def articles(request):
    return render(request, 'articles/articles.html')
