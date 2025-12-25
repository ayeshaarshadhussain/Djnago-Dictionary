from django.shortcuts import render, redirect
from .models import Word

def home(request):
    meaning = None
    searched_word = None

    if request.method == "POST":
        searched_word = request.POST.get('word')
        try:
            meaning = Word.objects.get(word__iexact=searched_word)
        except Word.DoesNotExist:
            meaning = "Word not found"

    return render(request, 'dictionary/home.html', {
    'meaning': meaning,
    'searched_word': searched_word
    })

def add_word(request):
    if request.method == "POST":
        word = request.POST.get('word')
        meaning = request.POST.get('meaning')

        if word and meaning:
            Word.objects.create(word=word, meaning=meaning)
            return redirect('home')

    # 👇 THIS LINE FIXES THE ERROR
    return render(request, 'dictionary/add_word.html')
