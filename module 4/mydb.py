import sqlalchemy as db

engine = db.create_engine('sqlite:///mydb.sqlite',echo=True)

connection = engine.connect()

meta = db.MetaData()

Disc = db.Table(
    'Disc', #name of the table
    meta, #meta data varialbe
    db.Column('name',db.String,primary_key=True),
    db.Column('manu',db.String,nullable=False),
    db.Column('speed',db.Integer,nullable=False)
)

meta.create_all(engine)
