from django.db import models
from datetime import date

# Create your models here.
class Todo(models.Model):
    titulo = models.CharField(verbose_name="Título", max_length=255, null=False, blank=False)
    data_criacao = models.DateTimeField(auto_now_add=True, null=False, blank=False)
    data_prazo = models.DateField(verbose_name="Data de Entrega", null=False, blank=False)
    data_entrega = models.DateField(null=True)

    class Meta:
        ordering = ["data_prazo"]

    def mark_has_complete(self):
        if not self.data_entrega:
            self.data_entrega = date.today()
            self.save