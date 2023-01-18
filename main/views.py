from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.core.exceptions import PermissionDenied
from .models import PhotoAvatar, UserProfile
from .forms import PhotoAvatarForm
from portfolio.models import Portfolio
from portfolio.forms import PortfolioForm
from django.http import HttpResponse, Http404


def home(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html', {})


def sign_up(request):
    if request.method == "POST":
        user = User()
        user.username = request.POST.get("username")
        user.email = request.POST.get("email")
        user.first_name = request.POST.get("first_name")
        user.last_name = request.POST.get("last_name")
        user.set_password(request.POST.get("password"))
        user.is_superuser = False
        user.is_staff = False
        user.is_active = True
        user.save()
        login(request, user)
        user_profile = UserProfile()
        user_profile.country = ' '
        user_profile.price = ' '
        user_profile.web_site = ' '
        user_profile.hour = ' '
        user_profile.language = ' '
        user_profile.phone = ' '
        user_profile.image_url = ' '
        user_profile.user_id = user.id
        user_profile.save()
        return redirect('/')
    else:
        return render(request, 'main/sign_up.html', {})


def sign_in(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user:
            login(request, user)
        return redirect('/')
    else:
        return render(request, 'main/sign_in.html', {})


def logout_view(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('/')


def edit_user(request, id):
    if request.user.is_authenticated:
        user = User.objects.get(id=id)
        user_plus = UserProfile.objects.get(user_id=id)
        return render(request, "main/sign_up.html", {
            'user': user,
            'user_plus': user_plus,
        })
    else:
        raise PermissionDenied


def update_user(request, id):
    if request.user.is_authenticated:
        user = User.objects.get(id=id)
        user.email = request.POST.get('email')
        user.username = request.POST.get('username')
        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.save()
        return redirect('/')


def change_password(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = User.objects.get(id=id)
            user.set_password(request.POST.get("password"))
            user.save()
            login(request, user)
            return redirect('/')
        else:
            return render(request, 'main/change_password.html')


def profile(request, id):
    if request.user.is_authenticated:
        profile_user = User.objects.get(id=id)
        user_plus = UserProfile.objects.all()
        if request.POST:
            form_portfolio = PortfolioForm(request.POST, request.FILES)
            if form_portfolio.is_valid():
                form_portfolio.save()
            return redirect('/')
        try:
            avatar = PhotoAvatar.objects.get(user_id=id)
            portfolio = Portfolio.objects.all()
        except:
            avatar = ''
            portfolio = ''
        if avatar is not None:
            return render(request, 'main/profile.html', {
                'profile_user': profile_user,
                'user_plus': user_plus,
                'avatar': avatar,
                'portfolio': portfolio,
                'form_portfolio': PortfolioForm,
            })
        else:
            return render(request, 'main/profile.html', {
                'profile_user': profile_user,
                'user_plus': user_plus,
                'form_portfolio': PortfolioForm,
            })
    else:
        raise PermissionDenied


def personal_data(request, id):
    if request.user.is_authenticated:
        user_plus = UserProfile.objects.get(user_id=id)
        user = User.objects.get(id=id)
        if request.POST:
            PhotoAvatar.objects.filter(user_id=id).delete()
            form_avatar = PhotoAvatarForm(request.POST, request.FILES)
            if form_avatar.is_valid():
                form_avatar.save()
            return redirect("/")
        try:
            avatar = PhotoAvatar.objects.get(user_id=id)
        except:
            avatar = ''

        if avatar is not None:
            return render(request, 'main/personal_data.html', {
                "avatar": avatar,
                "form_avatar": PhotoAvatarForm,
                "user_plus": user_plus,
                "user": user,
            })
        else:
            return render(request, 'main/personal_data.html', {
                "form_avatar": PhotoAvatarForm,
                "user_plus": user_plus,
                "user": user,
            })
    else:
        raise PermissionDenied


def personal_data_update(request, id):
    if request.user.is_authenticated:
        user_plus = UserProfile.objects.get(user_id=id)
        user = User.objects.get(id=id)
        if request.POST:
            user.username = request.POST.get("username")
            user.first_name = request.POST.get("first_name")
            user.last_name = request.POST.get("last_name")
            user.email = request.POST.get("email")
            user_plus.phone = request.POST.get("phone")
            user_plus.country = request.POST.get("country")
            user_plus.price = request.POST.get("price")
            user_plus.hour = request.POST.get("hour")
            user_plus.web_site = request.POST.get("web_site")
            user_plus.language = request.POST.get("language")
            user_plus.save()
            user.save()
            login(request, user)
            return redirect("/")

        return render(request, 'main/personal_data.html', {
                "user": user,
                "user_plus": user_plus,
            })
    else:
        raise PermissionDenied


def foto_profile(request, id, pk):
    photographer = User.objects.get(id=id)
    foto = Portfolio.objects.get(pk=pk)
    try:
        avatar = PhotoAvatar.objects.get(user_id=id)
        portfolio = Portfolio.objects.all()
    except:
        avatar = ''
        portfolio = ''
    return render(request, "main/foto_profile.html", {
        "foto": foto,
        "photographer": photographer,
        "avatar": avatar,
        "portfolio": portfolio,
    })


def delete_foto(request, id):
    Portfolio.objects.filter(id=id).delete()
    return redirect('/')