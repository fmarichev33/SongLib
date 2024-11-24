from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def search(request):
    query = request.GET.get('q')
    # Здесь вы можете добавить логику поиска
    # Например, поиск по базе данных или другому источнику данных
    # В данном примере просто возвращаем результаты поиска в шаблон search.html
    results = []  # Замените на реальные результаты поиска
    return render(request, 'search.html', {'query': query, 'results': results})