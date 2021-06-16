from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html')


def trigger_error_sentry(request):
    division_by_zero = 1 / 0
    return division_by_zero
