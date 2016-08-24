from django.shortcuts import render

# Create your views here.


def home(request):
	quote = 'athif valiyakath working in shaibig infosystem'
	return render(request, 'index.html', locals())
