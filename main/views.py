from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306152411',
        'name': 'Muhammad Vito Secona',
        'class': 'PBP F'
    }

    return render(request, "main.html", context)
