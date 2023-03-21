from django.shortcuts import render, redirect
from .models import Forum, ForumComment
from .forms import ForumForm, CommentForm
from main.models import PhotoAvatar
from django.views.generic import DetailView, UpdateView, DeleteView


def forum(request):
    visitor = request.user
    data = Forum.objects.order_by('-date')
    return render(request, 'forum/forum.html', {
        'data': data,
        "visitor": visitor,
    })


# class ForumDetailView(DetailView):
#     model = Forum
#     template_name = 'forum/detail_view.html'
#     context_object_name = 'forum'


def ForumDetailView(request, id):
    forum = Forum.objects.get(id=id)
    comments = ForumComment.objects.filter(cut_id=id)
    visitor = request.user
    try:
        avatars = PhotoAvatar.objects.all()
    except:
        avatars = ''
    return render(request, 'forum/detail_view.html', {
        'forum': forum,
        'comments': comments,
        'avatars': avatars,
        "visitor": visitor,
    })


def comment_crate(request, id):
    if request.method == 'GET':
        return render(request, 'forum/detail_view.html')
    else:
        comment = ForumComment()
        comment.full_text = request.POST.get('full_text')
        comment.cut_id = id
        comment.user = request.user
        comment.save()
        return redirect('forum_detail', id=id)


def comment_delete(request, id):
    temp_comment = ForumComment.objects.get(id=id)
    article = temp_comment.cut_id
    ForumComment(id=id).delete()
    return redirect("forum_detail", id=article)


def forum_create(request):
    error = ''
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('forum')
        else:
            error = 'Form was invalid, something wrong. Try again'

    form = ForumForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'forum/forum_create.html', data)


def forum_delete(request, id):
    Forum(id=id).delete()
    return redirect("forum")