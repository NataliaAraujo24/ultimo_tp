from typing import Optional
from pydantic import BaseModel, EmailStr


class Persona(BaseModel):
    id: Optional[int] = None
    nombre: str
    edad: int
    email: EmailStr

    # API
from fastapi import FastAPI, HTTPExcepcion
app = FastAPI()

#Base de datos simulada con un array
persona_db = []

#Crear Persona


@app.post("/personas/", response_model=Persona)
def crear_oersona(persona:Persona):
    persona.id = len(persona_db) +1
    return persona

# ver persona por id


@app.get("/persona/{persona_id}", response_model=Persona) 
def obtener_persona(persona_id:int): 
    for persona in persona_db:
        if persona.id == persona_id:
            return persona
        raise HTTPExcepcion(status_code=404, detail="Persona no encontrada") 

# Listar personas


@app.get("/personas/", respond_model=list[Persona])
def listar_persona(): 
    return persona_db

# Actualizar


@app.put("/personas/{persona_id}", response_model=Persona)
def actualizar_persona(persona_id: int, persona_actualizada: Persona):
    for index, persona in enumerate(personas_db):
        if persona.id == persona_id:
            personas_db[index] = persona_actualizada
            persona_actualizada.id = persona_id
            return persona_actualizada
    raise HTTPException(status_code=404, detail="Persona no encontrada")

# Eliminar


@app.delete("/personas/{persona_id}", response_model=dict)
def eliminar_persona(persona_id: int):
    for index, persona in enumerate(personas_db):
        if persona.id == persona_id:
            del personas_db[index]
            return {"detail": "Persona eliminada"}
    raise HTTPException(status_code=404, detail="Persona no encontrada")

    
    



    
    
