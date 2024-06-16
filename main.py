from database import session, engine, Base
from customer import Customer
from pharmacist import Pharmacist
from medicine import Medicine
from order import Order
from datetime import datetime

# Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)


def main():
    print("This is Dickson Murithi pharmacy feel much welcomed.")
    print("Welcome to Pharmacy Management System")
    print("1. Customer")
    print("2. Pharmacist")
    print("3. Medicine")
    print("4. Order")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        customer()
    elif choice == 2:
        pharmacist()
    elif choice == 3:
        medicine()
    elif choice == 4:
        order()
    elif choice == 5:
        exit()
    else:
        print("Invalid choice")

def customer():
    print("Welcome to Dickson Murithi pharmacy. We offer every type of medicine at affordable prices!")
    print("Welcome to Pharmacy Management System")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Delete Customer")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter customer name: ")
        email = input("Enter customer email: ")
        phone = input("Enter customer phone: ")
        address = input("Enter customer address: ")
        Customer.create_customer(name, email, phone, address)
        print("Customer added successfully!")
    elif choice == 2:
        customers = Customer.get_all_customers()
        for customer in customers:
            print(customer.id, customer.name, customer.email, customer.phone, customer.address)
    elif choice == 3:
        customer_id = int(input("Enter the ID of the customer you want to delete: "))
        if Customer.delete_customer(customer_id):
            print("Customer deleted successfully!")
        else:
            print("Customer not found!")
    elif choice == 4:
        exit()
    else:
        print("Invalid choice")

def medicine():
    print("Welcome to Pharmacy Management System")
    print("1. Add Medicine")
    print("2. View Medicines")
    print("3. Update Medicine")
    print("4. Delete Medicine")
    print("5. Search Medicine by Name")
    print("6. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        # Add Medicine
        name = input("Enter medicine name: ")
        price = float(input("Enter medicine price: "))
        quantity = int(input("Enter medicine quantity: "))
        new_medicine = Medicine(name, price, quantity)
        session.add(new_medicine)
        session.commit()
        print("Medicine added successfully!")
    elif choice == 2:
        # View Medicines
        medicines = Medicine.get_all_medicines()
        for medicine in medicines:
            print(medicine.id, medicine.name, medicine.price, medicine.quantity)
    elif choice == 3:
        # Update Medicine
        medicine_id = int(input("Enter the ID of the medicine you want to update: "))
        name = input("Enter new medicine name: ")
        price = float(input("Enter new medicine price: "))
        quantity = int(input("Enter new medicine quantity: "))
        if Medicine.update_medicine(medicine_id, name, price, quantity):
            print("Medicine updated successfully!")
        else:
            print("Medicine not found!")
    elif choice == 4:
        # Delete Medicine
        medicine_id = int(input("Enter the ID of the medicine you want to delete: "))
        if Medicine.delete_medicine(medicine_id):
            print("Medicine deleted successfully!")
        else:
            print("Medicine not found!")
    elif choice == 5:
        # Search Medicine by Name
        name = input("Enter the name of the medicine you want to search: ")
        medicine = Medicine.find_by_name(name)
        if medicine:
            print("Medicine found:")
            print(medicine.id, medicine.name, medicine.price, medicine.quantity)
        else:
            print("Medicine not found!")
    elif choice == 6:
        # Exit
        exit()
    else:
        print("Invalid choice")


def pharmacist():
    print("This is the pharmacist's office. How may I help you?")
    print("Welcome to Pharmacy Management System")
    print("1. Add Pharmacist")
    print("2. View Pharmacists")
    print("3. Delete Pharmacist")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        name = input("Enter pharmacist name: ")
        email = input("Enter pharmacist email: ")
        phone = input("Enter pharmacist phone: ")
        address = input("Enter pharmacist address: ")
        new_pharmacist = Pharmacist(name, email, phone, address)
        session.add(new_pharmacist)
        session.commit()
        print("Pharmacist added successfully!")
    elif choice == 2:
        pharmacists = session.query(Pharmacist).all()
        for pharmacist in pharmacists:
            print(f"ID: {pharmacist.id}, Name: {pharmacist.name}, Email: {pharmacist.email}, Phone: {pharmacist.phone}, Address: {pharmacist.address}")
    elif choice == 3:
        pharmacist_id = int(input("Enter the ID of the pharmacist you want to delete: "))
        if Pharmacist.delete_pharmacist(pharmacist_id):
            print("Pharmacist deleted successfully!")
        else:
            print("Pharmacist with that ID not found.")
    elif choice == 4:
        print("Exiting pharmacist's office.")

def order():
    print("we do deliverables countrywide!")
    print("Welcome to Pharmacy Management System")
    print("1. Add Order")
    print("2. View Orders")
    print("3. Delete Order")
    print("3. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        # Add customer
        name = input("Enter customer name: ")
        email = input("Enter customer email: ")
        phone = input("Enter customer phone: ")
        address = input("Enter customer address: ")
        new_customer = Customer(name, email, phone, address)
        session.add(new_customer)
        session.commit()
        print("Customer added successfully!")

        # Add medicine
        name = input("Enter medicine name: ")
        price = float(input("Enter medicine price: "))
        quantity = int(input("Enter medicine quantity: "))
        new_medicine = Medicine(name, price, quantity)
        session.add(new_medicine)
        session.commit()
        print("Medicine added successfully!")

        # Add pharmacist
        name = input("Enter pharmacist name: ")
        email = input("Enter pharmacist email: ")
        phone = input("Enter pharmacist phone: ")
        address = input("Enter pharmacist address: ")
        new_pharmacist = Pharmacist(name, email, phone, address)
        session.add(new_pharmacist)
        session.commit()
        print("Pharmacist added successfully!")

        # Add order
        order_quantity = int(input("Enter order quantity: "))
        pharmacist_name = input("Enter pharmacist name: ")  # Assuming you need to select pharmacist by name
        pharmacist = session.query(Pharmacist).filter_by(name=pharmacist_name).first()
        if pharmacist:
            new_order = Order(date=datetime.now(), customer_id=new_customer.id, medicine_id=new_medicine.id, pharmacist_id=pharmacist.id, quantity=order_quantity)
            session.add(new_order)
            session.commit()
            print("Order added successfully!")
        else:
            print("Pharmacist not found!")
    elif choice == 2:
        # View orders
        orders = session.query(Order).all()
        for order in orders:
            print(f"Customer: {order.customer.name}, Medicine: {order.medicine.name}, Quantity: {order.quantity}, Pharmacist: {order.pharmacists.name}")
    elif choice == 3:
        order_id = int(input("Enter the ID of the order you want to delete: "))
        if Order.delete_order(order_id):
            print("Order deleted successfully!")
        else:
            print("Order not found!")
    elif choice == 4:
        exit()
        
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
