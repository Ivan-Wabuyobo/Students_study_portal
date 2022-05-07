from django.shortcuts import render, redirect
from django.contrib import messages
from requests import post

from dashboard.forms import Create_homework, Create_notes
from youtube_search import YoutubeSearch
from PyDictionary import PyDictionary



from .models import *

# Create your views here.


def home(request):
    return render(request, "dashboard/home.html")


def notes(request):
    form = Create_notes()
    notes = Notes.objects.filter(user=request.user)
    context = {'notes': notes, 'form': form}

    if request.method == "POST":
        form = Create_notes(request.POST)
        if form.is_valid:
            user = request.user
            title = request.POST['title']
            description = request.POST['description']

            create_notes = Notes(user=user, title=title,
                                 description=description)
            create_notes.save()

            messages.info(request, "You have added some notes!!!!")

    return render(request, "dashboard/notes.html", context)

def notes_detail(request, pk):
    note = Notes.objects.filter(pk=pk)
    context = {"note":note}
    return render(request, 'dashboard/notes_detail.html', context)


def delete_notes(request, pk):
    note = Notes.objects.get(pk=pk).delete()
    messages.info(request, "Deleted")
    return redirect('notes')


def homework(request):
    if request.method == 'POST':
        form = Create_homework(request.POST)
        if form.is_valid:
            user = request.user
            title = request.POST['title']
            description = request.POST['description']
            subject = request.POST['subject']
            due = request.POST['due']
            is_completed = False

            create_homework = Homework(user=user, title=title, description=description,
                                       subject=subject, due=due)

            create_homework.save()

            return redirect('home-work')
        else:
            messages.info(
                request, "Please refill the form, there is an incorrect input!!!")
            

    else:
        form = Create_homework()
        homeworks = Homework.objects.filter(user=request.user)
        context = {'homeworks': homeworks, 'form': form}
        return render(request, "dashboard/homework.html", context)


def delete_homework(request, pk=None):
    Homework.objects.get(pk=pk).delete()
    return redirect('home-work')

def youtube(request):
    results = {}
    if request.method == "POST":
        search = request.POST['search']
        try:
            results = YoutubeSearch(search, max_results=100).to_dict()
            context = {"results":results}
            return render(request, "dashboard/youtube.html", context)
        except Exception:
            messages.info(request, "Please check your internet connection and try again.")
            context = {"results":results}
            return render(request, "dashboard/youtube.html",results)
    else:
        context = {"results":results}

        return render(request, "dashboard/youtube.html",results)


def dictionary(request):
    if request.method == "POST":
        search = request.POST['search']
        try:
            dictionary = PyDictionary()
            meaning = dictionary.meaning(search)
            print("===>>>TEST", meaning)


            return render(request, "dashboard/dictionary.html", {'meaning':meaning, 'search': search})
        except Exception:
            return render(request, "dashboard/dictionary.html")

    else:
        return render(request, "dashboard/dictionary.html")
 