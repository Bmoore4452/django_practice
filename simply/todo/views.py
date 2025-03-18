from django.shortcuts import render, redirect

from .forms import CreateUserForm


# Create your views here.
def homepage(request):
    return render(request, "index.html")


def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect
    context = {'form': form}
    return render(request, "register.html", context=context)


def login(request): ...


def dashboard(request): ...


def logout(request): ...
