from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import Questions, Interviews, CategoryQuestions
from .forms import QuestionsForm, SearchInterviewForm


def articles(request):
    categories = CategoryQuestions.objects.all()
    interviews = Interviews.objects.all().order_by("-id")
    questions = Questions.objects.all()
    my_list = []
    temp_list = []
    for question in questions:
        if question.cat_user_id in temp_list:
            continue
        else:
            my_list.append(question)
            temp_list.append(question.cat_user_id)
    return render(request, 'articles/articles.html', {
        "interviews": interviews,
        "questions": questions,
        "categories": categories,
        "my_list": my_list,
    })


def create_interview(request):
    new_interview = Interviews()
    new_interview.cat_user_id = request.user.id
    new_interview.save()
    return redirect("articles")


def open_interview(request, id):
    interview = Interviews.objects.get(id=id)
    questions = Questions.objects.filter(cat_interview_id=id)
    categories = CategoryQuestions.objects.all()
    creater = interview.cat_user_id
    visitor = request.user
    user = User.objects.get(id=creater)
    if request.method == "POST":
        form = QuestionsForm(request.POST)
        if form.is_valid():
            my_model = form.save(commit=False)
            my_model.cat_user_id = request.user.id
            my_model.cat_interview_id = id
            my_model.save()
            return redirect("open_interview", id=id)
    else:
        form = QuestionsForm()
    return render(request, "articles/open_interview.html", {
        "questions": questions,
        "categories": categories,
        "form": form,
        "visitor": visitor,
        "creater": creater,
        "interview": interview,
        "user": user,
    })


def delete_interview(request, id):
    Interviews(id=id).delete()
    return redirect("articles")


def search_interview(request):
    form = SearchInterviewForm(request.GET)
    users = []
    test = 0
    if form.is_valid():
        username = form.cleaned_data["username"]
        users = User.objects.filter(username__icontains=username)
        interviews = Interviews.objects.filter(cat_user_id=users[0].id)
        test = interviews[0].id
    return render(request, "articles/interview_search.html", {
        "form": form,
        "users": users,
        "test": test,
    })