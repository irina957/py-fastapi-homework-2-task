import datetime
from typing import Optional

from pydantic import BaseModel, Field


class CountrySchema(BaseModel):
    id: int
    name: Optional[str] = None
    code: str

    class Config:
        from_attributes = True


class NameSchema(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


GenreSchema = NameSchema
ActorSchema = NameSchema
LanguageSchema = NameSchema


class MovieListElement(BaseModel):
    id: int
    name: str
    date: datetime.date
    score: float
    overview: str

    class Config:
        from_attributes = True


class MoviePaginationResponse(BaseModel):
    movies: list[MovieListElement]
    prev_page: Optional[str] = None
    next_page: Optional[str] = None
    total_pages: int
    total_items: int


class MovieBase(BaseModel):
    name: str = Field(max_length=255)
    date: datetime.date
    score: float = Field(ge=0, le=100)
    overview: str
    status: str
    budget: float = Field(ge=0)
    revenue: float = Field(ge=0)


class MovieCreate(MovieBase):
    country: str
    genres: list[str]
    actors: list[str]
    languages: list[str]


class MovieDetail(MovieBase):
    id: int
    country: Optional[CountrySchema] = None
    genres: list[GenreSchema] = []
    actors: list[ActorSchema] = []
    languages: list[LanguageSchema] = []

    class Config:
        from_attributes = True


class MovieUpdate(BaseModel):
    name: Optional[str] = Field(None, max_length=255)
    date: Optional[datetime.date] = None
    score: Optional[float] = Field(None, ge=0, le=100)
    overview: Optional[str] = None
    status: Optional[str] = None
    budget: Optional[float] = Field(None, ge=0)
    revenue: Optional[float] = Field(None, ge=0)
