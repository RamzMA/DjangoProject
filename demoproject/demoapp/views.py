from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import AppForm
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return HttpResponse("This is the HomePage")

def success(request):
    return HttpResponse("Successful")

def about(request):
    content = {'about': "You can find out more on dishes by adding pasta,pizza or salad to the url instead of /about"}
    return render(request, 'about.html', content)

def dishes(request, dish):
    items = {
        'pasta': 'Pasta is a type of Italian food typically made from wheat flour and water, and sometimes eggs. It comes in various shapes and sizes, such as spaghetti, penne, and fusilli.',
        'pizza': 'Pizza is a popular Italian dish consisting of a round, flat base of dough topped with tomato sauce, cheese, and various toppings such as vegetables, meats, and herbs.',
        'salad': 'Salad is a dish typically made with a mixture of raw or cooked vegetables, fruits, and sometimes proteins like meat, cheese, or nuts. It is often served with a dressing or vinaigrette.'
    }

    description = items[dish]

    return HttpResponse(f"<h2> {dish} </h2>" + description)

def ApForm(request):
    form = AppForm()
    if request.method == 'POST':
        form = AppForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("success")
    context = {'form': form}
    return render(request, 'form.html', context)