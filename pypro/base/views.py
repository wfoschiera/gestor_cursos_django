from django.http import HttpResponse


# from django.shortcuts import render


# Create your views here.
def home(request):
    return HttpResponse('<html><body>Olá Django</body></html>', content_type='text/html')
  
  
def trigger_error_sentry(request):
    division_by_zero = 1 / 0
    return division_by_zero
  