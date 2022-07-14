from sqlalchemy.orm import sessionmaker
from Models.models import Base, Users, Disease
from datetime import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

username_input = input('Username: ')
password_input = input('Password: ')
name_input = input('Name: ')
surname_input = input('Surname: ')
patronymic_input = input('patronymic: ')
about_input = input('About: ')


engine = create_engine('sqlite:///../Policlinic.db', echo=True)
Base.metadata.create_all(engine)
sessionmaker = sessionmaker(bind=engine)
with sessionmaker.begin() as s:
    user = Users(username = username_input,
                 password = password_input,
                 name = name_input,
                 surname = surname_input,
                 patronymic = patronymic_input,
                 about = about_input,
                 doctor = 'tor',
                 # test_alembic = 12,
                 date_of_birth = datetime.now())
    disease = Disease(disease = 'alergicalllll')
    user.users_disease.append(disease)
    s.add(user, disease)
    s.commit()