from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import render
from .models import Portfolio
from main.models import PhotoAvatar


def portfolio(request):
    portfolio = Portfolio.objects.all().order_by('-id')
    return render(request, 'portfolio/portfolio.html', {
        "portfolio": portfolio,
    })


def foto_portfolio(request, id, pk):
    photographer = User.objects.get(id=id)
    foto = Portfolio.objects.get(pk=pk)
    try:
        avatar = PhotoAvatar.objects.get(user_id=id)
        portfolio = Portfolio.objects.all().order_by("-id")
    except:
        avatar = ''
        portfolio = ''
    return render(request, "portfolio/foto_portfolio.html", {
        "photographer": photographer,
        "foto": foto,
        "avatar": avatar,
        "portfolio": portfolio,
    })