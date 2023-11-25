from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, JsonResponse

# Create your views here.

def index(request):
    return render(request, "books/index.html", {})

def search_view(request):
    if request.method == 'POST':
        search_query = request.POST.get('search', '')
        
        # Process the search query (you can replace this with your logic)
        result = {'message': f'Searching for: {search_query}'}
        
        # Return a JSON response
        return JsonResponse(result)

    return render(request, 'your_app/your_template.html')  # Replace with the actual template path
