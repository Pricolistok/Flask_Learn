from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Users, Disease
from datetime import datetime


engine = create_engine('sqlite:///../Policlinic.db', echo=True)
Base.metadata.create_all(engine)
sessionmaker = sessionmaker(bind=engine)
with sessionmaker.begin() as s:
    user = Users(username = 'Brain_Belk',
                 password = '12345',
                 name = 'Brainin',
                 surname = 'Belcovichjk',
                 patronymic = 'Clifkl',
                 about = '12345678ikjhgtyu',
                 doctor = 'tor',
                 # test_alembic = 12,
                 date_of_birth = datetime.now())
    disease = Disease(disease = 'alergicalllll')
    user.users_disease.append(disease)
    s.add(user, disease)
    s.commit()
