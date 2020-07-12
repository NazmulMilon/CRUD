from django.shortcuts import render, redirect
from .models import Client
from .forms import ClientForm
# Create your views here.


def insert_view(request):
    form = ClientForm()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'insert.html', {'form': form})


def show_view(request):
    clients = Client.objects.all()
    return render(request,'show.html',{'clients': clients})


def delete_view(request,id):
    clients = Client.objects.get(id=id)
    clients.delete()
    return redirect('/')


def update_view(request,id):
    clients = Client.objects.get(id=id)
    form = ClientForm(request.POST, instance=clients)
    if form.is_valid():
        form.save(commit=True)
        return redirect('/')
    return render(request, 'update.html',{'clients':clients})
