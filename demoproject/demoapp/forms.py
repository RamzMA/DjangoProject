from django import forms

class ApplicationForm(forms.Form):
    name = forms.CharField(label="Name:", max_length=100)
    email = forms.EmailField(label="Email:",max_length=251)
    drinks = (('coffee', 'coffee'),('tea', 'tea'),('chantea', 'chantea'))
    drinksChoice = forms.ChoiceField(choices=drinks)