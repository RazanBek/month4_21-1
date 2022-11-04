from django.shortcuts import render, Http404
from datetime import datetime
from .models import Film, Director


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


def films_list_view(request):
    dict_ = {
        'film_list': Film.objects.all()
    }
    return render(request, 'films.html', context=dict_)


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