from sqlalchemy import create_engine
engine = create_engine ('mysql://root:icac104104@localhost/test1')
connection = engine.connect()

from mysql import MetaData, Table
metadata = MetaData()
census = Table ('census', metadata, autoload=True, autoload_with=engine)
