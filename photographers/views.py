from django.shortcuts import render
from django.contrib.auth.models import User
from main.models import UserProfile, PhotoAvatar
from portfolio.models import Portfolio


def photographers(request):
    photographers = User.objects.all()
    photographers_plus = UserProfile.objects.all()
    try:
        avatars = PhotoAvatar.objects.all()
        portfolio = Portfolio.objects.all()
    except:
        avatars = ''
        portfolio = ''

    if avatars is not None:
        return render(request, 'photographers/photographers.html', {
            "photographers": photographers,
            "photographers_plus": photographers_plus,
            "avatars": avatars,
            "portfolio": portfolio,
        })
    else:
        return render(request, 'photographers/photographers.html', {
            "photographers": photographers,
            "photographers_plus": photographers_plus,
        })


# def phone_card(request, id):
#     photographers_plus = UserProfile.objects.get(user_id=id)
#     return render(request, "photographers/phone.html", {
#         "photographers_plus": photographers_plus,
#     })
