from fastapi import APIRouter, HTTPException
from typing import List
from db_models.validation_models import CarVal,DilerVal
from db_models import db_manager
dilers_and_cars = APIRouter()

#dilers
@dilers_and_cars.get("/dilers",response_model=List[DilerVal])
async def get_dilers():
    return await db_manager.get_all_dilers()

@dilers_and_cars.post("/dilers", status_code=201)
async def add_diler(diler_load:DilerVal):
    diler = await db_manager.add_diler(diler_load)
    response = {
        "id" : diler,
        **diler_load.dict()
    }
    return response

@dilers_and_cars.put("/dilers/{id}")
async def update_diler(id:int,diler_load:DilerVal):
    dil=await db_manager.get_diler(id)
    if not dil:
        raise HTTPException(status_code=404,detail="Дилер не найден")
    update_data = diler_load.dict(exclude_unset=True)
    diler_in_db=DilerVal(**dil)
    updated_diler=diler_in_db.copy(update=update_data)
    return await db_manager.update_diler(id,updated_diler)

@dilers_and_cars.delete("/dilers/{id}")
async def delete_diler(id:int):
    dil = await db_manager.get_diler(id)
    if not dil:
        raise HTTPException(status_code=404,detail="Дилер не найден")
    return await db_manager.delete_diler(id)

#cars
@dilers_and_cars.get("/cars",response_model=List[CarVal])
async def get_cars():
    return await db_manager.get_all_cars()

@dilers_and_cars.post("/cars", status_code=201)
async def add_car(car_load:CarVal):
    car = await db_manager.add_car(car_load)
    response = {
        "id" : car,
        **car_load.dict()
    }
    return response

@dilers_and_cars.put("/cars/{id}")
async def update_car(id:int,car_load:CarVal):
    car=await db_manager.get_car(id)
    if not car:
        raise HTTPException(status_code=404,detail="Автомобиль не найден")
    update_data = car_load.dict(exclude_unset=True)
    car_in_db=CarVal(**car)
    updated_car=car_in_db.copy(update=update_data)
    return await db_manager.update_car(id,updated_car)

@dilers_and_cars.delete("/cars/{id}")
async def delete_car(id:int):
    car = await db_manager.get_car(id)
    if not car:
        raise HTTPException(status_code=404,detail="Автомобиль не найден")
    return await db_manager.delete_car(id)
