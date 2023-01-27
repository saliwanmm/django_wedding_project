from django.shortcuts import render
from django.contrib.auth.models import User
from main.models import UserProfile, PhotoAvatar
from portfolio.models import Portfolio


def photographers(request):
    photographers = User.objects.all()
    photographers_plus = UserProfile.objects.all()
    try:
        avatars = PhotoAvatar.objects.all()
        portfolio = Portfolio.objects.all().order_by("-id")
    except:
        avatars = ''
        portfolio = ''

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

# def phone_card(request, id):
#     photographers_plus = UserProfile.objects.get(user_id=id)
#     return render(request, "photographers/phone.html", {
#         "photographers_plus": photographers_plus,
#     })
