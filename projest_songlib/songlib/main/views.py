from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from .models import UploadedFile
from .forms import UploadFileForm

def home(request):
    files = UploadedFile.objects.all()
    paginator = Paginator(files, 10)  # Показывать 10 файлов на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'home.html', {'page_obj': page_obj})

def contact(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UploadFileForm()
    return render(request, 'contact.html', {'form': form})

def search(request):
    query = request.GET.get('q')
    if query:
        files = UploadedFile.objects.filter(title__icontains=query)
    else:
        files = UploadedFile.objects.all()
    paginator = Paginator(files, 10)  # Показывать 10 файлов на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'search.html', {'page_obj': page_obj, 'query': query})

def file_detail(request, file_id):
    file = get_object_or_404(UploadedFile, id=file_id)
    return render(request, 'file_detail.html', {'file': file})