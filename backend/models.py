from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class ToolData(Base):
    __tablename__ = 'tool_data'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    data = Column(String)

engine = create_engine('postgresql://user:password@localhost/tat2db')
Session = sessionmaker(bind=engine)
