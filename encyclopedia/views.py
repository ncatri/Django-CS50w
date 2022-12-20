from django.shortcuts import render
from django.http import HttpResponse

from . import util
import markdown2


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