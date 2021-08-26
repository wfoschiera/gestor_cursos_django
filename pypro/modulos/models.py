from django.db import models
from ordered_model.models import OrderedModel

from django.utils.translation import gettext_lazy as _


# Create your models here.


class Modulo(OrderedModel):
    titulo = models.CharField(max_length=64)
    publico = models.TextField(default="")
    descricao = models.TextField(default="")
    order = models.PositiveIntegerField(_("order"), editable=False, db_index=True, default="")

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.titulo
