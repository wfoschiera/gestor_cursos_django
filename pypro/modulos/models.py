from django.db import models
from django.urls import reverse
from ordered_model.models import OrderedModel

from django.utils.translation import gettext_lazy as _


# Create your models here.


class Modulo(OrderedModel):
    titulo = models.CharField(max_length=64)
    publico = models.TextField()
    descricao = models.TextField()
    order = models.PositiveIntegerField(_("order"), editable=False, db_index=True)
    slug = models.SlugField()

    class Meta(OrderedModel.Meta):
        pass

    def __str__(self):
        return self.titulo

    def get_absolute_url(self):
        return reverse("modulos:detalhe", kwargs={"slug": self.slug})
