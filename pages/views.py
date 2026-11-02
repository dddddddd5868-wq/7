from django.shortcuts import render
from config.models import Service


def home(request):
	return render(request, 'index.html', {'services': Service.objects.all()[:3]})


def about(request):
	return render(request, 'about.html')


def services(request):
	return render(request, 'services.html', {'services': Service.objects.all()})


def contacts(request):
	return render(request, 'contacts.html')
