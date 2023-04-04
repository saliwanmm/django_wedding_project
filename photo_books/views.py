from django.shortcuts import render, redirect
from .models import PhotoBook, PhotoBookPortfolio, PhotoBookComment
from main.models import PhotoAvatar
from django.contrib.auth.models import User
from .forms import PhotoBookForm, PhotoBookPortfolioForm


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
    insider = request.user

    if request.method == "POST":
        form = PhotoBookPortfolioForm(request.POST, request.FILES)
        if form.is_valid():
            my_model = form.save(commit=False)
            my_model.user = request.user
            my_model.cut_id = pk
            my_model.save()
            return redirect("story", id=id, pk=pk)

    form = PhotoBookPortfolioForm()

    try:
        avatars_comment = PhotoAvatar.objects.all()
    except:
        avatars_comment = ''
    return render(request, 'photo_books/foto_photo_book.html', {
        "form": form,
        "user": user,
        "foto": foto,
        "portfolio": portfolio,
        "comments": comments,
        "avatars_comment": avatars_comment,
        "insider": insider,
    })


def story_create(request):
    if request.method == "POST":
        form = PhotoBookForm(request.POST, request.FILES)
        if form.is_valid():
            my_model = form.save(commit=False)
            my_model.user = request.user
            my_model.save()
            return redirect("photo_books")
    else:
        form = PhotoBookForm()
    return render(request, "photo_books/photo_book_create.html", {
        "form": form,
    })


def delete_story(request, id):
    PhotoBook(id=id).delete()
    return redirect("photo_books")


def delete_story_portfolio(request, id):
    temp_photo = PhotoBookPortfolio.objects.get(id=id)
    PhotoBookPortfolio(id=id).delete()
    return redirect("story", id=temp_photo.user_id, pk=temp_photo.cut_id)


def photo_book_comment_crate(request, id):
    if request.method == 'GET':
        return render(request, 'photo_books/foto_photo_book.html')
    else:
        comment = PhotoBookComment()
        comment.full_text = request.POST.get('full_text')
        comment.cut_id = id
        comment.user = request.user
        photo_with_comment = PhotoBook.objects.get(id=id)
        pk = photo_with_comment.user_id
        comment.save()
        return redirect('story', id=pk, pk=id)


def foto_photobook_daughter(request, id, pk):
    photo = PhotoBookPortfolio.objects.get(id=pk)
    story_id = id
    creater_story_id = photo.user_id
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
        "creater_story_id": creater_story_id,
        "story_id": story_id,
    })


def delete_comment_photobook(request, id):
    temp_comment = PhotoBookComment.objects.get(id=id)
    cut_id = temp_comment.cut_id
    photo_book_with_comment = PhotoBook.objects.get(id=cut_id)
    user_id = photo_book_with_comment.user_id
    PhotoBookComment(id=id).delete()
    return redirect("story", id=user_id, pk=cut_id)