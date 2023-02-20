from django.shortcuts import render

# Create your views here.
def home(request):
    nama = {'name':'Yumana'}
    return render(request, 'filmicquote\home.html', nama)