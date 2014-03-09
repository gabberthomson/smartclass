from django.db import models

# Create your models here.

class AnnoScolastico(models.Model):
    anni = models.CharField(max_length=10)

class Scuola(models.Model):
    nome = models.CharField(max_length=100)

class Classe(models.Model):
    nome = models.CharField(max_length=100)
    scuola = models.ForeignKey(Scuola)

class Materia(models.Model):
    nome = models.CharField(max_length=100)
    
class Studente(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    data_nascita = models.DateField()
    
    class Meta:
        unique_together = ("nome", "cognome", "data_nascita") 

class DettaglioStudente(models.Model):
    studente = models.ForeignKey(Studente)
    annoscolastico = models.ForeignKey(AnnoScolastico)
    classe = models.ForeignKey(Classe)
    scuola = models.ForeignKey(Scuola)

    class Meta:
        unique_together = ("studente", "annoscolastico", "classe", "scuola") 

    
