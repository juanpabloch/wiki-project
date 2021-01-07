from django.shortcuts import render, redirect
import random

from . import util

from .forms import New_Entry_Form, Edit_form
import markdown2

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, entry):
    list_entries = util.list_entries()
    if entry in list_entries:
        data = util.get_entry(entry)
        context = {
            "title": entry,
            "data": markdown2.markdown(data),
        }
        return render(request, "encyclopedia/entry.html", context)
    else:
        context = {
            "data": None,
        }
        return render(request, "encyclopedia/entry.html", context)
    

def Entry_Form(request):
    form = New_Entry_Form(request.POST or None)
    if form.is_valid():
        title = form.cleaned_data["title"]
        content = form.cleaned_data["content"]
        util.save_entry(title, content)
        return redirect(f'wiki/{title}')
    context = {
        "form":form,
    }
    return render(request, "encyclopedia/new-entry.html", context)

def random_page(request):
    lista = util.list_entries()
    entry = random.choice(lista)
    return redirect(f'wiki/{entry}')

def search_entry(request):
    if request.method == 'POST':
        search = request.POST["q"].lower()
        entries = []
        qs = util.list_entries()
        for entry in qs:
            entries.append(entry.lower())
        if search.lower() in entries:
            return redirect(f'wiki/{search}')
        else:
            filtros = filter_entries(entries, search)
            context = {
                "filtros": filtros,
            }
            return render(request, "encyclopedia/search.html", context)

    return render(request, "encyclopedia/search.html", {})


""" function to filter words """
def filter_entries(entries, search):
    list_entry = []
    for item in entries:
        if search in item:
            list_entry.append(item.capitalize())

    return list_entry


def edit_entry(request, entry):
    data = util.get_entry(entry)
    if request.method == 'POST':
        form = Edit_form(request.POST or None)
        if form.is_valid():
            content = form.cleaned_data["content"]
            util.save_entry(entry, content)
            return redirect(f'/wiki/{entry}')
    else:
        edit = Edit_form(initial={'content':data})
        context = {
        "form": edit,
        "title": entry,
    }
    return render(request, "encyclopedia/edit.html", context)