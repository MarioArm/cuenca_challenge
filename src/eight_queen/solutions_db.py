from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine("postgresql+pg8000://root:root@localhost:5432/solutions")
Session = sessionmaker(bind=engine)
session: Session = Session()

Base = declarative_base()
