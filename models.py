from datetime import datetime

from pydantic import BaseModel


class CityModel(BaseModel):
    id: int
    name: str
    additional_info: str


class TemperatureModel(BaseModel):
    id: int
    city_id: int
    date_time: datetime
    temperature: float
