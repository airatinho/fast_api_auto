from sqlalchemy import (Column, Integer, MetaData, String, Table,Boolean,Date,
                        create_engine, orm,ForeignKey)
from databases import Database

DATABASE_URI = 'postgresql://postgres:1@localhost/dilers_and_cars'
metadata = MetaData()
engine = create_engine(DATABASE_URI,echo=False)

dilers = Table(
    "dilers",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("name",String(100)),
    Column("address",String(100))
)
cars = Table(
    "cars",
    metadata,
    Column("id",Integer,primary_key=True),
    Column("name",String),
    Column("sold",Boolean, default=False),
    Column("year_of_manufacture",Date),
    Column("color",String),
    Column("broken",Boolean, default=False),
    Column("price",Integer, default=100000),
    Column("num_owners",Integer, default=0),
    Column("diler_id",Integer, ForeignKey('dilers.id', ondelete='cascade'),nullable=False),

)
orm.relationship("Dilers", foreign_keys="cars.diler_id")
database=Database(DATABASE_URI)