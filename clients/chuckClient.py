"""
=============================================================================
CLIENTE HTTP PARA LA API DE CHUCK NORRIS
=============================================================================

Este módulo contiene la clase ChuckNorrisClient que se encarga de realizar
las peticiones HTTP a la API externa de Chuck Norris.

Documentación oficial: https://api.chucknorris.io/

=============================================================================
"""

import httpx
from typing import Optional
from fastapi import HTTPException
from appsettings import AppSettings

class ChuckNorrisClient:
  """
  Cliente HTTP para interactuar con la API de Chuck Norris.
  """

  def __init__(self):
    pass

  async def get_random_joke(self, category: Optional[str] = None, http_client: httpx.AsyncClient = None) -> dict:
    """
    Obtiene un chiste aleatorio de Chuck Norris.
    Args:
      category (str, optional): Categoría del chiste.
      http_client (httpx.AsyncClient): Cliente HTTP asíncrono.
    """
    url = f"{AppSettings.CHUCK_BASE_URL}/jokes/random"
    params = {}
    if category:
      params["category"] = category
      
    response = await http_client.get(url, params=params, timeout=AppSettings.TIMEOUT_SECONDS)
    
    if response.status_code == 404:
       raise HTTPException(status_code=404, detail="No se encontró chiste (o categoría inválida).")
    elif response.status_code != 200:
       raise HTTPException(status_code=response.status_code, detail="Error al comunicarse con la API de Chuck Norris")

    return response.json()

  async def get_categories(self, http_client: httpx.AsyncClient) -> list:
    """
    Obtiene la lista de categorías disponibles.
    Args:
      http_client (httpx.AsyncClient): Cliente HTTP asíncrono.
    """
    url = f"{AppSettings.CHUCK_BASE_URL}/jokes/categories"
    response = await http_client.get(url, timeout=AppSettings.TIMEOUT_SECONDS)
    
    if response.status_code != 200:
      raise HTTPException(status_code=response.status_code, detail="Error al obtener las categorías")

    return response.json()