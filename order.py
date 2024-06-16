from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base
from database import session

class Order(Base):
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True)
    date = Column(Date, nullable=False)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    medicine_id = Column(Integer, ForeignKey('medicines.id'), nullable=False)
    pharmacist_id = Column(Integer, ForeignKey('pharmacists.id'), nullable=False)
    quantity = Column(Integer, nullable=False)

    customer = relationship("Customer", back_populates="orders",overlaps="customers")
    medicine = relationship("Medicine", back_populates="orders",overlaps="medicines")
    pharmacists = relationship("Pharmacist", back_populates="orders",overlaps="pharmacists")
    

    def __init__(self, date, customer_id, medicine_id,pharmacist_id, quantity):
        self.date = date
        self.customer_id = customer_id
        self.medicine_id = medicine_id
        self.pharmacist_id = pharmacist_id
        self.quantity = quantity
        session.add(self)
        session.commit()

    @staticmethod
    def get_all_orders():
        orders = session.query(Order).all()
        return orders
        
    @staticmethod
    def get_order_by_id(id):
        order = session.query(Order).filter_by(id=id).first()
        return order
    @staticmethod
    def delete_order(order_id):
        order = session.query(Order).filter_by(id=order_id).first()
        if order:
            session.delete(order)
            session.commit()
            return True
        else:
            return False
    @staticmethod
    def initialize_data():
        if not session.query(Order).filter_by(date='2020-01-01').first():
            Order(date='2020-01-01', customer_id=1, medicine_id=1, quantity=10)
        session.commit()