from django.shortcuts import render

# Create your views here.
def render_index(request):
    return render(request, 'index.html')

def render_acesso(request):
    cadastrado = False
    if cadastrado:
        return render(request, 'home.html')
    else:
        return render(request, 'cadastrar.html')

def render_home(request):
    return render(request, 'home.html')