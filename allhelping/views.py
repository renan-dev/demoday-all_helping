from django.shortcuts import render
from .models import Ajudado, Ajudante, Match, Mensagem
import random

# Create your views here.
def render_index(request):
    return render(request, 'index.html')

def acesso(request):
    i = 0
    if request.method == 'POST' and request.POST.get('gerarChat') is None:
        if request.POST.get('Ajudar') == 'Ajudar':
            pessoa = Ajudante()
        elif request.POST.get('Ajuda') == 'Ajuda':
            pessoa = Ajudado()

        pessoa.telefone = request.POST.get('telefone')
        pessoa.nome = request.POST.get('nome')
        pessoa.sobrenome = request.POST.get('sobrenome')
        pessoa.email = request.POST.get('email')
        pessoa.save()

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
            if match_bd is None or request.POST.get('gerarChat'):
                match = Match()
                match.ID_ajudante = pessoa
                match.ID_ajudado = Ajudado.objects.order_by("?").first()
                
                while Match.objects.filter(ID_ajudado=match.ID_ajudado) and i <= 50:
                    match = Match()
                    match.ID_ajudante = pessoa
                    match.ID_ajudado = Ajudado.objects.order_by("?").first()
                    i += 1
                if i <= 50:
                    match.save()
            match_bd = Match.objects.filter(ID_ajudante=pessoa.id).all()
            n = random.randrange(0, Ajudado.objects.count())
            return render(request, 'home.html', {'matchs': match_bd, 'ajudante': True, 'n': i, 'papel': papel})
        else:
            match_bd = Match.objects.filter(ID_ajudado=pessoa.id).first()
            if match_bd is None or request.POST.get('gerarChat'):
                match = Match()
                match.ID_ajudante = Ajudante.objects.first()
                match.ID_ajudado = pessoa
                match.save()
            match_bd = Match.objects.filter(ID_ajudado=pessoa.id).all()
            return render(request, 'home.html', {'matchs': match_bd, 'ajudado': True})

def render_cadastro(request):
    i=0
    return render(request, 'cadastrar.html')

def render_home(request):
    return render(request, 'home.html')

def render_chat(request):
    match = Match.objects.filter(id=request.GET.get('MatchID')).first()
    papel = request.GET.get('papel')
    i = -1
    if papel == 'ajudante':
        pessoa = match.ID_ajudante.nome
    elif papel == 'ajudado':
        pessoa = match.ID_ajudado.nome
    if request.method == 'POST':
        mensagem = Mensagem()
        mensagem.mensagem = request.POST.get('mensagem')
        mensagem.remetente = pessoa
        mensagem.ID_match = match
        mensagem.save()
        i -= 1
    mensagem = Mensagem.objects.filter(ID_match=request.GET.get('MatchID'))
    return render(request, 'chat.html', {'mensagens': mensagem, 'papel': papel, 'match': match,'i': i})
