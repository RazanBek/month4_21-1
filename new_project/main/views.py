from django.shortcuts import render, Http404, redirect
from datetime import datetime
from .models import Film, Director
from .forms import FilmForm, DirectorForm, UserCreateForm, UserLoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


def logout_view(request):
    logout(request)
    return redirect('/films/')


def login_view(request):
    context = {
        'form': UserLoginForm()
    }
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username, password=password)
            if not user:
                return redirect('/login/')
            else:
                login(request, user)
                return redirect('/films/')
    return render(request, 'login.html', context)


def register_view(request):
    context = {
        'form': UserCreateForm()
    }
    if request.method == 'POST':
        form = UserCreateForm(data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            User.objects.create_user(username=username, password=password)
            return redirect('/login/')
        context['form'] = form
    return render(request, 'register.html', context=context)


def film_create_view(request):
    context = {
        'form': FilmForm()
    }
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/films/')
        else:
            context['form'] = form
    return render(request, 'create_film.html', context)


def director_create_view(request):
    context = {
        'form': DirectorForm()
    }
    if request.method == 'POST':
        form = DirectorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/films/')
        else:
            context['form'] = form
    return render(request, 'create_director.html', context)


def date_now_view(request):
    date = datetime.now()
    context = {
        'year': date.year,
        'month': date.month,
        'day': date.day,
    }

    return render(request, 'date_now.html', context=context)


def about_us_view(request):
    return render(request, 'about_us.html')


PAGE_SIZE = 3


def films_list_view(request):
    page = int(request.GET.get('page', 1))
    all_film = Film.objects.all()
    films = all_film[(page - 1) * PAGE_SIZE: page * PAGE_SIZE]
    film_list = all_film[PAGE_SIZE * (page - 1): PAGE_SIZE * page]
    total = all_film.count()
    pages_amount = total // PAGE_SIZE + 1 if total % PAGE_SIZE == 0 else total // PAGE_SIZE + 1
    dict_ = {
        'film_list': film_list,
        'buttons': [i for i in range(1, pages_amount + 1)],
        'page': page,
        'prev_page': page - 1,
        'next_page': page + 1,
        'pages': (total + PAGE_SIZE - 1) // PAGE_SIZE,
        'films': films
    }
    return render(request, 'films.html', context=dict_)


def director_list_view(request):
    dict_ = {
        'director_list': Director.objects.all()
    }
    return render(request, 'director.html', context=dict_)


def film_detail_view(request, id):
    dict_ = {}
    try:
        film = Film.objects.get(id=id)
    except Film.DoesNotExist:
        raise Http404('Film not found')
    dict_['film_detail'] = film
    dict_['directors'] = Director.objects.filter(id=id)
    return render(request, 'detail.html', context=dict_)


def director_films_view(request, director_id):
    try:
        director = Director.objects.get(id=director_id)
    except Director.DoesNotExist:
        raise Http404
    context = {
        'director': director
    }
    return render(request, 'director_films.html', context=context)


def search_view(request):
    search_word = request.GET.get('search_word', '')
    context = {
        'films': Film.objects.filter(title__icontains=search_word),
        'search_word': search_word
    }
    return render(request, 'search.html', context)