from pydantic import BaseModel, Field


class Form(BaseModel):
    name:str = Field(..., min_length=3, max_length=10)
    lastname:str = Field(..., min_length=3, max_length=10)
    dni:str = Field(...,pattern=r'\d{8}[A-Z]$')

    class Config:
        json_schema_example = {
            "name": "John",
            "lastname": "Doe",
            "dni": "12345678A"
        }