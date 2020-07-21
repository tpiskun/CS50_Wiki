from django import forms
from django.forms import Textarea
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.urls import reverse
from django.core.files.storage import default_storage
from django.contrib import messages
from collections import Counter
from django.utils.safestring import mark_safe
import re
import markdown2
import random

from . import util

wikis = util.list_entries()

class TitleForm(forms.Form):
    TitleForm = forms.CharField(label="Wiki Title", widget=forms.TextInput(attrs={'size': '40'}))

class ContentForm(forms.Form):
    ContentForm = forms.CharField(label="", widget=forms.Textarea(attrs={'style': 'width: 35em; height:25em;' }))

class EditForm(forms.Form):
    EditForm = forms.CharField(label="Edit Wiki:", widget=forms.Textarea(attrs={'style': 'width: 45em; height:35em;' }))

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
    })

def page(request, page):
    #if request.method=="GET":
    if default_storage.exists(f"entries/{page}.md"):
        return Convert_Entry(request=request, entry=page)
    else:
        return render(request, f"encyclopedia/Error.html", {
            "message": "No Such Wiki Exists."
        })

def Search(request):
    if request.method == "POST":
        query=request.POST.get('q')
        count = 0
        for i in wikis:
            match = re.search(query, i)
            if match is not None:
                count += 1
                result = i
        if count >=1:
            search = page(request=request, page=result)
        else:
            search = render(request, f"encyclopedia/Error.html", {
                "message": f"No Such Wiki for {query} Exists."
            })
        return search

def Convert_Entry(request, entry):
    md_file = util.get_entry(entry)
    converted_file = markdown2.markdown(md_file)
    return render(request, f"encyclopedia/Page_Title.html", {
        "title": entry,
        "content": converted_file
    })

def New_Page(request):
        #new_page_form = form.cleaned_data["new_page_form"]
    if request.method == "POST":
        #title = TitleForm(request.POST)
        #content = request.POST.get('content')
        content_form = ContentForm(request.POST)
        form = TitleForm(request.POST)
        if form.is_valid() and content_form.is_valid():
            title = form.cleaned_data["TitleForm"]
            content = content_form.cleaned_data["ContentForm"]
            print(title)
            print(content)
            count = 0
            for wiki in wikis:
                title_match = re.search(title, wiki)
                if title_match is not None:
                    count += 1
            if count >= 1:
                    messages.error(request, 'Title already exists.')
                    result = HttpResponseRedirect(reverse("encyclopedia:new_page"))
            else:
                    content_string= "# " + title + "\n" + content
                    print(content_string)
                    util.save_entry(title = title, content=content_string)
                    result = Convert_Entry(request=request, entry = title)
            return result

    else:
        return render(request, f"encyclopedia/New_Page.html", {
            "form" : TitleForm(),
            "content_form": ContentForm()
        })

def Random_Page(request):
    random_page = random.choice(wikis)
    return page(request = request, page = random_page)

def Edit_Page(request, edit_page):
    if request.method == "GET":
        initial_data = util.get_entry(edit_page)
        data = {'EditForm' : initial_data}
        form = EditForm(data)
        return render(request, f"encyclopedia/Edit_Page.html", {
            "edit_page": edit_page,
            "form" : form
        })
    if request.method == "POST":
        form = EditForm(request.POST)
        if form.is_valid():
            edited_wiki = form.cleaned_data["EditForm"]
            util.save_entry(title = edit_page, content=edited_wiki)
            #HttpResponseRedirect(reverse("encyclopedia:page", kwargs={'page':edit_page}))
            return Convert_Entry(request=request, entry = edit_page)
