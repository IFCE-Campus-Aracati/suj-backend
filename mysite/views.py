""" Minhas views básicas.

    Servindo o arquivo principal do site.
"""
from django.shortcuts import render


# Create your views here.
def home(request):
    """Página inicial.

    Args:
        request (Http request): requisição vinda do navegador

    Returns:
        HttpResponse: Renderização da página inicial do site.
    """
    return render(request, "mysite/index.html")
