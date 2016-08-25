from django.shortcuts import render

# Create your views here.


def home(request):
	quote = 'athif valiyakath lives in banglore'
	return render(request, 'index.html', locals())
