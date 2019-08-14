from django.shortcuts import render
from .models import Ajudado, Ajudante, Match, Mensagem

# Create your views here.
def render_index(request):
    return render(request, 'index.html')

def acesso(request):
    ajudado_bd = Ajudado.objects.filter(telefone=request.GET.get('telefone')).first()
    telefone = request.GET.get('telefone')
    if ajudado_bd is not None:
        match_bd = Match.objects.filter(ID_ajudado=ajudado_bd.id).first()
        if match_bd is None:
            match = Match()
            match.ID_ajudante = Ajudante.objects.first()
            match.ID_ajudado = ajudado_bd
            match.save()
            match_bd = Match.objects.filter(ID_ajudado=ajudado_bd.id).first()
        return render(request, 'home.html', {'ajudante': match_bd.ID_ajudante.nome, 'ajudado': match_bd.ID_ajudado.nome})
    else:
        return render(request, 'cadastrar.html', {'telefone': telefone})

def render_cadastro(request):
    ajudado = Ajudado()
    if request.method == 'POST':
        ajudado.telefone = request.POST.get('telefone')
        ajudado.nome = request.POST.get('nome')
        ajudado.sobrenome = request.POST.get('sobrenome')
        ajudado.email = request.POST.get('email')
        ajudado.save()
        return render(request, 'home.html', {'ajudado': ajudado})
    return render(request, 'cadastrar.html')

def render_home(request):
    return render(request, 'home.html')