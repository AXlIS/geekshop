from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from authapp.forms import UserLoginForm


def login(request):
    form = UserLoginForm(data=request.POST)
    if request.method == 'POST' and form.is_valid():
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user and user.is_active:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('main'))

    context = {'form': form}
    return render(request, 'authapp/login.html', context)
