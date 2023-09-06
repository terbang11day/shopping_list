from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Thariq Ziyad Al Farizi',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)