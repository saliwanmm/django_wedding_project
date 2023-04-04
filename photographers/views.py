from django.shortcuts import render
from django.contrib.auth.models import User
from main.models import UserProfile, PhotoAvatar
from portfolio.models import Portfolio
from .forms import UserSearchForm


def photographers(request):
    photographers = User.objects.all()
    photographers_plus = UserProfile.objects.all()
    try:
        portfolio = Portfolio.objects.all().order_by("-id")
    except:
        portfolio = ''
    try:
        avatars = PhotoAvatar.objects.all()
    except:
        avatars = ''

    if avatars is not None:
        return render(request, 'photographers/photographers.html', {
            "photographers": photographers,
            "photographers_plus": photographers_plus,
            "avatars": avatars,
            "portfolio": portfolio,
            "flag": 1,
        })
    else:
        return render(request, 'photographers/photographers.html', {
            "photographers": photographers,
            "photographers_plus": photographers_plus,
        })


def foto_photographer(request, id, pk):
    photographer = User.objects.get(id=id)
    photo = Portfolio.objects.get(pk=pk)
    try:
        portfolio = Portfolio.objects.filter(user_id=id).order_by("-id")
        portfolio_new = []
        flag = False
        for port in portfolio:
            if flag == False:
                if port.id == photo.id:
                    portfolio_new.append(port)
                    flag = True
            else:
                portfolio_new.append(port)
        for port in portfolio:
            if flag == True:
                if port.id != photo.id:
                    portfolio_new.append(port)
                else:
                    flag = False
            else:
                break
        portfolio = portfolio_new
    except:
        portfolio = ''
    return render(request, "photographers/foto_photographer.html", {
        "photo": photo,
        "portfolio": portfolio,
        "photographer": photographer,
    })


def find_photographer(request):
    form = UserSearchForm(request.GET)
    users = []
    if form.is_valid():
        last_name = form.cleaned_data["last_name"]
        users = User.objects.filter(last_name__icontains=last_name)
    return render(request, "photographers/find-photographer.html", {
        "form": form,
        "users": users,
    })
