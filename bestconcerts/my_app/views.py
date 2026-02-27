from django.shortcuts import render
from django.http import HttpResponse

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

def concert_index(request):
    return render(request, 'concerts/index.html', {'concerts': concerts})

