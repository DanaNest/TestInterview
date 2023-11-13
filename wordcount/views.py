from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
import string

words = []

def load(filename):
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip().lower()
            line = line.translate(str.maketrans('', '', string.punctuation))
            words.extend(line.split())

def index(request):
    if request.method == 'POST':
        if 'file' in request.FILES:
            file = request.FILES['file']
            fs = FileSystemStorage()
            fs.save(file.name, file)
            load(fs.path(file.name))
            return redirect('/')
        elif 'word' in request.POST:
            word = request.POST['word']
            count = words.count(word)
            return render(request, 'index.html', {'count': count})
        elif 'clear' in request.POST:
            words.clear()
            return redirect('/')
    return render(request, 'index.html')