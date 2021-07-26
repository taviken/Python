from django.shortcuts import (
    render,
    redirect,
)
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request=request,
                             message=f'Account created for {username}')
            response = redirect(to='blog-home')
        else:
            response = redirect(to='blog-home')
    else:
        form = UserRegisterForm()
        context = {'form': form}
        response = render(request=request,
                          template_name='users/register.html',
                          context=context)
    return response
