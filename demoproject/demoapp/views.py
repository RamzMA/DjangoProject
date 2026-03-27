from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world. This is the index view of the django app!")

def dishes(request, dish):
    items = {
        'pasta': 'Pasta is a type of Italian food typically made from wheat flour and water, and sometimes eggs. It comes in various shapes and sizes, such as spaghetti, penne, and fusilli.',
        'pizza': 'Pizza is a popular Italian dish consisting of a round, flat base of dough topped with tomato sauce, cheese, and various toppings such as vegetables, meats, and herbs.',
        'salad': 'Salad is a dish typically made with a mixture of raw or cooked vegetables, fruits, and sometimes proteins like meat, cheese, or nuts. It is often served with a dressing or vinaigrette.'
    }

    description = items[dish]

    return HttpResponse(f"<h2> {dish} </h2>" + description)