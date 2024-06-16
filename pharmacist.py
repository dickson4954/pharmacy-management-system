from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from database import Base
from database import session

class Pharmacist(Base):
    __tablename__ = 'pharmacists'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False, unique=True)
    phone = Column(String(20), nullable=False)
    address = Column(String(250), nullable=False)
    orders = relationship("Order", back_populates="pharmacists")

   
    
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address

        session.add(self)
        session.commit()
    @staticmethod
    def get_all_pharmacists():
        pharmacists = session.query(Pharmacist).all()
        return pharmacists
    @staticmethod
    def get_pharmacist_by_id(id):
        pharmacist = session.query(Pharmacist).filter_by(id=id).first()
        return pharmacist
    @staticmethod
    def delete_pharmacist(pharmacist_id):
        pharmacist = session.query(Pharmacist).filter_by(id=pharmacist_id).first()
        if pharmacist:
            session.delete(pharmacist)
            session.commit()
            return True
        else:
            return False
        
    @staticmethod
    def initialize_data():
        if not session.query(Pharmacist).filter_by(name='brandon').first():
            Pharmacist(name='brandon', email="brandon@gmail.com", phone=12345678, address="mombasa")
        
        session.commit()