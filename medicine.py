from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import relationship
from database import session
from database import Base
from order import Order




class Medicine(Base):
    __tablename__ = 'medicines'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    price = Column(Float, nullable=False)
    quantity = Column(Integer, nullable=False) 

    orders = relationship("Order", back_populates="medicine")

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
        session.add(self)
        session.commit()

    @staticmethod
    def get_all_medicines():
        medicines = session.query(Medicine).all()
        return medicines
    @staticmethod
    def find_by_id(medicine_id):    
        medicine = session.query(Medicine).filter_by(id=medicine_id).first()
        return medicine

    @staticmethod
    def find_by_name(name):
        medicine = session.query(Medicine).filter_by(name=name).first()
        return medicine
    @staticmethod
    def update_medicine(medicine_id, name, price, quantity):
        medicine = session.query(Medicine).filter_by(id=medicine_id).first()
        if medicine:
            medicine.name = name
            medicine.price = price
            medicine.quantity = quantity
            session.commit()
            return True
        else:
            return False
    @staticmethod
    def delete_medicine(medicine_id):
        medicine = session.query(Medicine).filter_by(id=medicine_id).first()
        if medicine:
          
          session.query(Order).filter_by(medicine_id=medicine_id).delete()
          session.delete(medicine)
          session.commit()
          return True
        else:
          return False
            
    
    @staticmethod 
    def initialize_data():
        if not session.query(Medicine).filter_by(id=1).first():
            Medicine(name="Medicine1", price=100, quantity=100)
            session.commit()
            
            




    
