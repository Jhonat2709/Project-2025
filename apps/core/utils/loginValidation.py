from django.http import HttpResponseRedirect
from django.contrib.auth import login, authenticate
from django.shortcuts import render
from django.urls import reverse

def loginProcess(request):
    user = authenticate(request, username=request.POST['username'], password=request.POST['password'])

    if user is None:
        return render(request, 'core/login.html', {'error': "Nombre de usuario o contraseña incorrecto"})
    login(request, user)
    return HttpResponseRedirect(reverse('dashboard'))