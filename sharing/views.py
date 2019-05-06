from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'authorization/login.html')

def register(request):
    return render(request, 'authorization/register.html')

def store(request):
    if request.method == 'POST':
        print(request.POST)
    return render(request, 'authorization/register.html')