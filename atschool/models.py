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

    class Meta:
        unique_together = ("studente", "annoscolastico", "classe") 

class Professore(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    data_nascita = models.DateField()

    
class ProfessoreMateria(models.Model):
    prof = models.ForeignKey(Professore)
    materia = models.ForeignKey(Materia)
    classe = models.ForeignKey(Classe)
    annoscolastico = models.ForeignKey(AnnoScolastico)

    class Meta:
        unique_together = ("prof", "materia", "classe") 

class TipoVerifica(models.Model):
    tipo = models.CharField(max_length = 20, primary_key = True)
    
class Verifica(models.Model):
    studente = models.ForeignKey(Studente)
    prof = models.ForeignKey(Professore)
    materia = models.ForeignKey(Materia)
    tipo = models.ForeignKey(TipoVerifica)
    voto = models.CharField(max_length = 20)
    nota  = models.CharField(max_length = 200, null = True)
    data = models.DateField()
    annoscolastico = models.ForeignKey(AnnoScolastico)
    class Meta:
        unique_together = ("studente", "prof", "data", "tipo") 

class Assenze(models.Model):
    data = models.DateField()
    studente = models.ForeignKey(Studente)
    annoscolastico = models.ForeignKey(AnnoScolastico)
    
    class Meta:
        unique_together = ("data", "studente", "annoscolastico") 

class Giustificazione(models.Model):
    assenza = models.ForeignKey(Assenze)
    nota = models.CharField(max_length = 200, null = True)

from django.contrib import admin

admin.site.register(Classe)
admin.site.register(Scuola)
admin.site.register(Materia)
admin.site.register(Verifica)
admin.site.register(TipoVerifica)
admin.site.register(Studente)
admin.site.register(Professore)
admin.site.register(ProfessoreMateria)
admin.site.register(DettaglioStudente)
admin.site.register(AnnoScolastico)
admin.site.register(Assenze)
admin.site.register(Giustificazione)

    