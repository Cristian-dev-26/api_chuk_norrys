"""
=============================================================================
CONTROLADOR DE CHUCK NORRIS (CAPA DE PRESENTACIÓN)
=============================================================================

Este módulo contiene los endpoints HTTP para consultar chistes de Chuck Norris.

Endpoints disponibles:
- GET /api/chuck/random - Chiste aleatorio
- GET /api/chuck/categories - Categorías disponibles
- GET /api/chuck/random?category={category} - Chiste por categoría

=============================================================================
"""

import httpx
from fastapi import APIRouter, Query
from typing import List, Optional
from services.chuckServices import ChuckService
from DTOs.chuckDtos import JokeDTO

# Creamos el router con prefijo para agrupar todos los endpoints de Chuck
router = APIRouter(prefix="/api/chuck", tags=["Chuck Norris"])

@router.get("/random", response_model=JokeDTO)
async def get_random_joke(category: Optional[str] = Query(None, description="Categoría opcional para filtrar el chiste")):
  """
  Obtiene un chiste aleatorio de Chuck Norris.
  
  Args:
    category (str, optional): Categoría del chiste (ej: "dev", "movie", "food")
  
  Returns:
    JokeDTO: El chiste obtenido
  """
  async with httpx.AsyncClient() as http_client:
    service = ChuckService()
    joke = await service.get_random_joke(category, http_client)
    return joke

@router.get("/categories", response_model=List[str])
async def get_categories():
  """
  Obtiene la lista de categorías disponibles para los chistes.
  
  Returns:
    List[str]: Lista de categorías
  """
  async with httpx.AsyncClient() as http_client:
    service = ChuckService()
    categories = await service.get_categories(http_client)
    return categories