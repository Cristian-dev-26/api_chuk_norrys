"""
=============================================================================
DTOs (DATA TRANSFER OBJECTS) - MODELOS DE DATOS
=============================================================================

Este módulo contiene los DTOs (Data Transfer Objects) utilizados para
estructurar los datos de respuesta de la API de Chuck Norris.

=============================================================================
"""

from pydantic import BaseModel, Field
from typing import List, Optional

class JokeDTO(BaseModel):
  """
  DTO para representar un chiste de Chuck Norris.
  """
  id: str = Field(..., description="ID único del chiste")
  value: str = Field(..., description="Contenido del chiste de Chuck Norris")
  url: str = Field(..., description="URL del chiste en api.chucknorris.io")
  icon_url: str = Field(..., description="URL del icono de Chuck Norris")
  categories: List[str] = Field(default=[], description="Lista de categorías a las que pertenece el chiste")
  created_at: str = Field(..., description="Fecha de creación del chiste")
  updated_at: str = Field(..., description="Fecha de actualización del chiste")

  class Config:
    json_schema_extra = {
      "example": {
        "id": "abc12345",
        "value": "Chuck Norris divide por cero.",
        "url": "https://api.chucknorris.io/jokes/abc12345",
        "icon_url": "https://assets.chucknorris.host/img/avatar/chuck-norris.png",
        "categories": ["dev"],
        "created_at": "2020-01-05 13:42:24.147092",
        "updated_at": "2020-01-05 13:42:24.147092"
      }
    }