from django.http import HttpResponse
from django.shortcuts import render


def portfolio(request):
    # return HttpResponse('Portfolio')
    return render(request, 'portfolio.html')
