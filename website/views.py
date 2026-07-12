import os
import requests
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render


def home(request):
    context = {
        "github": settings.GITHUB,
        "kaggle": settings.KAGGLE,
        "leetcode": settings.LEETCODE,
        "hackerrank": settings.HACKERRANK,
    }
    return render(request, 'home.html', context)

def about(request):
    context = {
        "btechcollege": settings.BTECHCOLLEGE,
        "school": settings.SCHOOL,
    }
    return render(request, 'about.html', context)

def skills(request):
    return render(request, "skills.html")

def projects(request):
    return render(request, 'projects.html')

def contact(request):
    context = {
        "email": settings.EMAIL,
        "linkedin": settings.LINKEDIN,
        "github": settings.GITHUB,
        "kaggle": settings.KAGGLE,
    }
    return render(request, "contact.html", context)
