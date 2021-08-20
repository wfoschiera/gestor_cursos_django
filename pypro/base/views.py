from django.shortcuts import render

from pypro.modulos import facade


# Create your views here.


def home(request):
    return render(request, "base/home.html", context={"MODULOS": facade.listar_modulos_ordenados()})


def trigger_error_sentry(request):
    division_by_zero = 1 / 0
    return division_by_zero
