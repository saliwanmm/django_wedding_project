from django.shortcuts import render, redirect
from .models import PhotoBook, PhotoBookPortfolio, PhotoBookComment
from main.models import PhotoAvatar
from django.contrib.auth.models import User


def photo_books(request):
    photobooks = PhotoBook.objects.all().order_by('-id')
    return render(request, 'photo_books/photo_books.html', {
        "photobooks": photobooks
    })


def story(request, id, pk):
    portfolio = PhotoBookPortfolio.objects.filter(cut_id=pk).order_by('-id')
    comments = PhotoBookComment.objects.filter(cut_id=pk)
    foto = PhotoBook.objects.get(id=pk)
    user = User.objects.get(id=id)
    try:
        avatars_comment = PhotoAvatar.objects.all()
    except:
        avatars_comment = ''
    return render(request, 'photo_books/foto_photo_book.html', {
        "user": user,
        "foto": foto,
        "portfolio": portfolio,
        "comments": comments,
        "avatars_comment": avatars_comment,
    })


def photo_book_comment_crate(request, id):
    if request.method == 'GET':
        return render(request, 'photo_books/foto_photo_book.html')
    else:
        comment = PhotoBookComment()
        comment.full_text = request.POST.get('full_text')
        comment.cut_id = id
        comment.user = request.user
        comment.save()
        return redirect('photo_books')


def foto_photobook_daughter(request, id, pk):
    photo = PhotoBookPortfolio.objects.get(id=pk)
    try:
        portfolio = PhotoBookPortfolio.objects.filter(cut_id=id).order_by("-id")
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
    return render(request, "photo_books/foto_photo_book_daughter.html", {
        "portfolio": portfolio,
        "photo": photo,
    })