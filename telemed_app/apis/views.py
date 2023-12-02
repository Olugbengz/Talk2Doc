from django.http import JsonResponse

# Create your views here.

def home(request):
    return JsonResponse({'Telemed': 'The app for the physicians'})