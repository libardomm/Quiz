from django.db import models

class Question(models.Model):
    content=models.CharField(max_length=1000,
                             help_text="Ingrese  la pregunta que quiere mostrar"
    )
    def __str__(self):
        return self.content

class Answer(models.Model):
    question = models.ForeignKey(Question,  on_delete=models.CASCADE, verbose_name=("Question"))
    content = models.CharField(max_length=1000,
                               blank=False,
                               help_text=("Ingrese la respuesta"),
                               verbose_name=("Content"))

    correct = models.BooleanField(blank=False,
                              default=False,
                              help_text=("¿esta es la respuesta correcta?"),
                              verbose_name=("Correct"))
    def __str__(self):
        return self.content

class Quiz(models.Model):
    nombre=models.CharField(max_length=1000,
                            blank=False,
                            help_text=("Nombre de Quiz"),
                            verbose_name=("Nombre"))
    questions=models.ManyToManyField(Question)

    def __str__(self):
        return self.nombre
