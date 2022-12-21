import re
import os

from django.core.files.base import ContentFile
from django.core.files.storage import default_storage


def list_entries():
    """
    Returns a list of all names of encyclopedia entries.
    """
    _, filenames = default_storage.listdir("entries")
    return list(sorted(re.sub(r"\.md$", "", filename)
                for filename in filenames if filename.endswith(".md")))


def save_entry(title, content):
    """
    Saves an encyclopedia entry, given its title and Markdown
    content. If an existing entry with the same title already exists,
    it is replaced.
    """
    print(f"in save_entry(), content: {content}")
    filename = f"entries/{title}.md"
    if default_storage.exists(filename):
        default_storage.delete(filename)
        print(f"deleted {filename}")
    default_storage.save(filename, ContentFile(content))
    print(f"saved {filename}")


def get_entry(title):
    """
    Retrieves an encyclopedia entry by its title. If no such
    entry exists, the function returns None.
    """
    entry = ""
    entries_filenames = os.listdir("entries")
    print(f"in get_entry(), title: {title}")
    for file in entries_filenames:
#        f = file.lower().split(".")[0]
        if title == file.split(".")[0]:
            entry = file
            break
    if not entry:
        return None
    try:
        
        f = default_storage.open(f"entries/{entry}")
        return f.read().decode("utf-8")
    except FileNotFoundError:
        return None

def search(query):
    print(f"in search(), query--> {query}")
    filenames = list_entries()
    print(f"in search(), filenames--> {filenames}")
    res = [file for file in filenames if query.lower() in file.lower() ]
    print(f"in search(), res--> {res}")
    return res