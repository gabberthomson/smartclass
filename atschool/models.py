from django.db import models

# Create your models here.

class AnnoScolastico(models.Model):
    anni = models.CharField(max_length=10)
    
    def __unicode__(self):
        return self.anni
    
    class Meta:
        verbose_name = "Anno Scolastico"
        verbose_name_plural = "Anni Scolastici"


class Scuola(models.Model):
    nome = models.CharField(max_length=100)
    
    def __unicode__(self):
        return self.nome

    class Meta:
        verbose_name = "Scuola"
        verbose_name_plural = "Scuole"

class Classe(models.Model):
    nome = models.CharField(max_length=100)
    scuola = models.ForeignKey(Scuola)
    
    def __unicode__(self):
        return self.nome + " - " + self.scuola.nome

    class Meta:
        verbose_name = "Classe"
        verbose_name_plural = "Classi"

class Materia(models.Model):
    nome = models.CharField(max_length=100)

    def __unicode__(self):
        return self.nome
    
    class Meta:
        verbose_name = "Materia"
        verbose_name_plural = "Materie"

class Studente(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    data_nascita = models.DateField()

    def __unicode__(self):
        return self.nome + " " + self.cognome + " - " + str(self.data_nascita)
    
    class Meta:
        unique_together = ("nome", "cognome", "data_nascita") 
        verbose_name = "Studente"
        verbose_name_plural = "Studenti"

class DettaglioStudente(models.Model):
    studente = models.ForeignKey(Studente)
    annoscolastico = models.ForeignKey(AnnoScolastico)
    classe = models.ForeignKey(Classe)

    def __unicode__(self):
        return str(self.studente)+ " - " + str(self.annoscolastico) + " - " + str(self.classe)

    class Meta:
        unique_together = ("studente", "annoscolastico", "classe") 
        verbose_name_plural = "Dettagli studenti"

class Professore(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)
    data_nascita = models.DateField()

    def __unicode__(self):
        return self.nome+ " " + self.cognome + " - " + str(self.data_nascita)

    class Meta:
        verbose_name = "Professore"
        verbose_name_plural = "Professori"
    
class ProfessoreMateria(models.Model):
    prof = models.ForeignKey(Professore)
    materia = models.ForeignKey(Materia)
    classe = models.ForeignKey(Classe)
    annoscolastico = models.ForeignKey(AnnoScolastico)

    def __unicode__(self):
        return str(self.prof) + " - " + str(self.materia) + " - " + str(self.classe) + " - " + str(self.annoscolastico)

    class Meta:
        verbose_name = "Professore e Materia"
        verbose_name_plural = "Professori e Materie"
        unique_together = ("prof", "materia", "classe") 

class TipoVerifica(models.Model):
    tipo = models.CharField(max_length = 20, primary_key = True)
    
    def __unicode__(self):
        return self.tipo

    class Meta:
        verbose_name = "Tipo Verifica"
        verbose_name_plural = "Tipi Verifica"
  
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
        verbose_name = "Verifica"
        verbose_name_plural = "Verifiche"

    def __unicode__(self):
        return str(self.studente) + " - " + str(self.materia) + " - " + str(self.tipo) + " - Voto: " + self.voto + " - " + self.data

class Assenza(models.Model):
    data = models.DateField()
    studente = models.ForeignKey(Studente)
    annoscolastico = models.ForeignKey(AnnoScolastico)
    
    def __unicode__(self):
        return str(self.studente) + " - " + str(self.data)

    class Meta:
        verbose_name = "Assenza"
        verbose_name_plural = "Assenze"
        unique_together = ("data", "studente", "annoscolastico") 

class Giustificazione(models.Model):
    assenza = models.ForeignKey(Assenza)
    nota = models.CharField(max_length = 200, null = True)

    def __unicode__(self):
        return "Giustifica: " + str(self.assenza)

    class Meta:
        verbose_name = "Giustificazione"
        verbose_name_plural = "Giustificazioni"

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
admin.site.register(Assenza)
admin.site.register(Giustificazione)
