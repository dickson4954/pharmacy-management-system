from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import relationship
from database import Base
from database import session
from order import Order


class Customer(Base):
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, nullable=False)
    phone = Column(String, nullable=False)
    address = Column(String, nullable=False)
    orders = relationship("Order", backref="customers")
    def __init__(self, name, email, phone, address):
        self.name = name
        self.email = email
        self.phone = phone
        self.address = address
        session.add(self)
        session.commit()
    @staticmethod
    def create_customer(name, email, phone, address):
        new_customer = Customer(name, email, phone, address)
        session.add(new_customer)
        session.commit()
        return new_customer    
    @staticmethod
    def get_all_customers():
        customers = session.query(Customer).all()
        return customers

    @staticmethod
    def delete_customer(customer_id):
        customer = session.query(Customer).filter_by(id=customer_id).first()
        if customer:
            session.delete(customer)
            session.commit()
            return True
        else:
            return False
        
        
    @staticmethod
    def initialize_data():
        if not session.query(Customer).filter_by(id=1).first():
            Customer(name="Customer1", email="email1", phone="phone1", address="address1")
            session.commit()  