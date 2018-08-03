from sqlalchemy import create_engine
from mysql import MetaData, Table
engine = create_engine ('mysql://root:icac104104@localhost/test1')
connection = engine.connect()


metadata = MetaData()
census = Table ('census', metadata, autoload=True, autoload_with=engine)
