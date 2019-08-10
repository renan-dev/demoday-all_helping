from django.db import models

from django.db import models


class Ajudado(models.Model):

  nome = models.CharField(
    max_length=255,
    verbose_name='Nome')
  email = models.EmailField(
    max_length=255,
    verbose_name='E-mail')
  telefone = models.CharField(
    max_length=255,
    verbose_name='Telefone')

  ativo = models.BooleanField(
    default=True
  )
  data_de_criacao = models.DateField(
    auto_now_add=True
  )

  def __str__(self):
    return self.nome + ' ' + self.email

class Ajudante(models.Model):
  nome = models.CharField(
    max_length=255,
    verbose_name='Nome')
  email = models.EmailField(
    max_length=255,
    verbose_name='E-mail')
  telefone = models.CharField(
    max_length=255,
    verbose_name='Telefone')

  ativo = models.BooleanField(
    default=True
  )
  data_de_criacao = models.DateField(
    auto_now_add=True
  )

  def __str__(self):
    return self.nome + ' ' + self.email

  
class Match(models.Model):
    ID_ajudante = models.ForeignKey(Ajudante)
    ID_ajudado = models.ForeignKey(Ajudado)

class Mensagem(models.Model):
  mensagem = models.CharField(
    max_length=255,
    verbose_name='Mensagem')
  remetente = models.EmailField(
    max_length=255,
    verbose_name='Remetente')
  telefone = models.CharField(
    max_length=255,
    verbose_name='Telefone')
  data = models.DateField(
    auto_now_add=True)
  ID_match = models.ForeignKey(Match)
    
    