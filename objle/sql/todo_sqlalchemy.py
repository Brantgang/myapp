from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base=declarative_base()


class User(Base):
    __tablename__='man'
    name=Column(String(20),primary_key=True)
    sex=Column(String(3))

engine = create_engine('mysql+pymysql://root: @localhost:3306/hello')
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


session= DBSession()
#new_user=User(name='12',sex='1')
#session.add(new_user)
#session.commit()
user=session.query(User).all()
for i in range(len(user)):
    print(user.__getitem__(i).name)
session.close()