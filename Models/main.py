from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Users, Disease
from datetime import datetime
from sqlalchemy.orm import Session


engine = create_engine('sqlite:///../Policlinic.db', echo=True)
Base.metadata.create_all(engine)
sessionmaker = sessionmaker(bind=engine)
with sessionmaker.begin() as s:
    user = Users(username = '45',
                 password = '12345',
                 name = 'Brainin',
                 surname = 'Belcovichjk',
                 patronymic = 'Clifkljkkphi;boj;lbijpbinkhjvoip',
                 about = '12345678ikjhgtyu',
                 doctor = 'tor',
                 # test_alembic = 12,
                 date_of_birth = datetime.now())
    disease = Disease(disease = 'alergicalllll')
    user.users_disease.append(disease)
    s.add(user, disease)
    s.commit()
# session = Session(bind=engine)
# print(session.query(Users.patronymic).filter(Users.username == 'Cliff1223344').all())