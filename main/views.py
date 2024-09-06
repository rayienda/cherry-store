from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'product' : 'Cherry Heels',
        'price': '270.000',
        'description': 'Very comfortable and stylish for everyday use.'
    }

    return render(request, "main.html", context)