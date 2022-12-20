from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from . import util
import markdown2
from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import os

def index(request):
    print(f"in views, request: {request}")
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    print(f"in entry(), title --> {title}")
    title = title.lower()
    return render(request, "encyclopedia/entry.html", {
        "title": title,
        "content": markdown2.markdown(util.get_entry(title))
    })

def search_result(request):
    query = request.GET.get("q")
    if query in util.list_entries():
        return entry(request, query)
    else:
        return render(request, "encyclopedia/search.html", {
            "query": query,
            "result": util.search(query)
        })


def validate_entry_is_new(title):
    if f"{title}.md"in os.listdir("entries"):
        raise ValidationError(
            _('%(title)s already exists'),
            params={'title': title},
        )


class NewEntryForm(forms.Form):
    title = forms.CharField(label="Title", validators=[validate_entry_is_new])
    content = forms.CharField(widget=forms.Textarea)

def new_entry(request):
    if request.method == 'POST':
        form = NewEntryForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            content = form.cleaned_data["content"]
            util.save_entry(title, content)
            return (HttpResponseRedirect(f"{title}"))
        else:
            return render(request, "encyclopedia/new_entry.html", {
                "form": form
            })

    return render(request, "encyclopedia/new_entry.html", {
        "form": NewEntryForm()
    })