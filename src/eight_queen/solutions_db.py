from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

engine = create_engine(f"postgresql+pg8000://root:root@{os.getenv('CUENCA_DB_HOST', default='localhost')}:5432/solutions")
Session = sessionmaker(bind=engine)
session: Session = Session()

Base = declarative_base()
