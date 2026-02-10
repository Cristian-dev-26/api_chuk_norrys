"""
=============================================================================
SERVICIO DE CHUCK NORRIS (CAPA DE LÓGICA DE NEGOCIO)
=============================================================================

Este módulo contiene la clase ChuckService que implementa la lógica de
negocio para obtener chistes de Chuck Norris.

=============================================================================
"""

import httpx
from clients.chuckClient import ChuckNorrisClient
from DTOs.chuckDtos import JokeDTO

class ChuckService:
  """
  Servicio principal para obtener chistes de Chuck Norris.
  """

  def __init__(self):
    self.client = ChuckNorrisClient()

  async def get_random_joke(self, category: str, http_client: httpx.AsyncClient) -> JokeDTO:
    """
    Obtiene un chiste aleatorio, opcionalmente filtrado por categoría.
    """
    joke_data = await self.client.get_random_joke(category, http_client)
    
    return JokeDTO(
      id=joke_data.get("id"),
      value=joke_data.get("value"),
      url=joke_data.get("url"),
      icon_url=joke_data.get("icon_url"),
      categories=joke_data.get("categories", []),
      created_at=joke_data.get("created_at"),
      updated_at=joke_data.get("updated_at")
    )

  async def get_categories(self, http_client: httpx.AsyncClient) -> list[str]:
    """
    Obtiene la lista de categorías de chistes disponibles.
    """
    categories = await self.client.get_categories(http_client)
    return categories
