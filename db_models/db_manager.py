from db_models.validation_models import CarVal, DilerVal
from db_models.db_models import cars,dilers,database


#dilers
async def get_all_dilers():
    query = dilers.select()
    return await database.fetch_all(query=query)

async def get_diler(id:int):
    query = dilers.select(dilers.c.id==id)
    return await database.fetch_one(query)

async def add_diler(diler_load:DilerVal):
    query = dilers.insert().values(**diler_load.dict())
    return await database.execute(query)

async def update_diler(id:int,diler_load:DilerVal):
    query = dilers.update().where(dilers.c.id==id).values(**diler_load.dict())
    return await database.execute(query=query)

async def delete_diler(id:int):
    query = dilers.delete().where(dilers.c.id==id)
    return await database.execute(query=query)


#cars
async def get_all_cars():
    query = cars.select()
    return await database.fetch_all(query=query)

async def get_car(id:int):
    query = cars.select(cars.c.id == id)
    return await database.fetch_one(query)


async def add_car(car_load:CarVal):
    query = cars.insert().values(**car_load.dict())
    return await database.execute(query)

async def update_car(id:int,car_load:CarVal):
    query = cars.update().where(cars.c.id == id).values(**car_load.dict())
    return await database.execute(query=query)

async def delete_car(id:int):
    query = cars.delete().where(cars.c.id==id)
    return await database.execute(query=query)