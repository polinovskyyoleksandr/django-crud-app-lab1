from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Concert
from django.contrib.auth.views import LoginView
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class Concert:
    def __init__(self, artist, genre, description, year):
        self.artist = artist
        self.genre = genre
        self.description = description
        self.year = year

concerts = [
    Concert('Bad Omens', 'Metal', 'Was really cool in Manchester!', 2025),
    Concert('Nayt', 'Rap', 'Needed to hear him live.', 2025),
]

@login_required
def concert_index(request):
    concerts = Concert.objects.filter(user=request.user)
    return render(request, 'concerts/index.html', {'concerts': concerts})

def concert_detail(request, concert_id):
    concert = Concert.objects.get(id=concert_id)
    return render(request, 'concerts/detail.html', {'concert': concert})

class ConcertCreate(LoginRequiredMixin, CreateView):
    model = Concert
    fields = '__all__'
    
    def form_valid(self, form):
        form.instance.user = self.request.user  
        return super().form_valid(form)

class ConcertUpdate(UpdateView):
    model = Concert
    fields = '__all__'

class ConcertDelete(DeleteView):
    model = Concert
    success_url = '/concerts/'

class Home(LoginView):
    template_name = 'home.html'

def signup(request):
    error_message = ''
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('concert-index')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'signup.html', context)






