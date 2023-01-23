from django.http import Http404
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Portfolio, PortfolioComment
from main.models import PhotoAvatar


def portfolio(request):
    portfolio = Portfolio.objects.all().order_by('-id')
    return render(request, 'portfolio/portfolio.html', {
        "portfolio": portfolio,
    })


def foto_portfolio(request, id, pk):
    photographer = User.objects.get(id=id)
    foto = Portfolio.objects.get(pk=pk)
    comments = PortfolioComment.objects.filter(cut_id=pk)
    try:
        avatar = PhotoAvatar.objects.get(user_id=id)
        portfolio = Portfolio.objects.all().order_by("-id")
        avatars_comment = PhotoAvatar.objects.all()
    except:
        avatar = ''
        portfolio = ''
        avatars_comment = ''
    return render(request, "portfolio/foto_portfolio.html", {
        "photographer": photographer,
        "foto": foto,
        "avatar": avatar,
        "portfolio": portfolio,
        "comments": comments,
        "avatars_comment": avatars_comment,
    })


def portfolio_comment_crate(request, id):
    if request.method == 'GET':
        return render(request, 'portfolio/foto_portfolio.html')
    else:
        comment = PortfolioComment()
        comment.full_text = request.POST.get('full_text')
        comment.cut_id = id
        comment.user = request.user
        comment.save()
        return redirect('portfolio')
