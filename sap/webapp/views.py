from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def bienvenido(request):
    return render(request, 'EstudiantesTdea.html')

def despedirse(request):
    return HttpResponse('Despedida de django')