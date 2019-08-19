from django.shortcuts import render
from .models import Ajudado, Ajudante, Match, Mensagem

# Create your views here.
def render_index(request):
    return render(request, 'index.html')

def acesso(request):
        ajudado_bd = Ajudado.objects.filter(telefone=request.GET.get('telefone')).first()
        ajudante_bd = Ajudante.objects.filter(telefone=request.GET.get('telefone')).first()
        telefone = request.GET.get('telefone')

        if ajudado_bd is not None:
            pessoa = ajudado_bd
            papel = 'ajudado'
        elif ajudante_bd is not None:
            pessoa = ajudante_bd
            papel = 'ajudante'
        else:
            return render(request, 'cadastrar.html', {'telefone': telefone})
        
        if pessoa is not None:
            if papel == 'ajudante':
                match_bd = Match.objects.filter(ID_ajudante=pessoa.id).first()
                if match_bd is None:
                    match = Match()
                    match.ID_ajudante = pessoa
                    match.ID_ajudado = Ajudado.objects.first()
                    match.save()
            else:
                match_bd = Match.objects.filter(ID_ajudado=pessoa.id).first()
                if match_bd is None:
                    match.ID_ajudante = Ajudante.objects.first()
                    match.ID_ajudado = pessoa
                    match.save()
                    match_bd = Match.objects.filter(ID_ajudado=pessoa.id).first()
        if papel == 'ajudante':
            match_bd = Match.objects.filter(ID_ajudante=pessoa.id).all()
            return render(request, 'home.html', {'matchs': match_bd, 'ajudante': True})
        if papel == 'ajudado':
            match_bd = Match.objects.filter(ID_ajudado=pessoa.id).all()
            return render(request, 'home.html', {'matchs': match_bd, 'ajudado': True})

def render_cadastro(request):
    if request.method == 'POST':
        
        if request.POST.get('Ajudar') == 'Ajudar':
            pessoa = Ajudante()
        elif request.POST.get('Ajuda') == 'Ajuda':
            pessoa = Ajudado()

        pessoa.telefone = request.POST.get('telefone')
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.email = request.POST.get('email')
        pessoa.save()
        
        return render(request, 'home.html', {'pessoa': pessoa})
    return render(request, 'cadastrar.html')

def render_home(request):
    return render(request, 'home.html')

def render_chat(request):
    return render(request, 'chat.html')