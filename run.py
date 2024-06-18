from app.settings import ENGINE
from commands.fill import CustomerFill, EmployeeFill, OrderFill
from models.session import Session

if __name__ == '__main__':
    session = Session(ENGINE)

    fill_customers = CustomerFill()
    fill_employees = EmployeeFill()
    fill_orders = OrderFill()

    fill_customers.run(session)
    fill_employees.run(session)
    fill_orders.run(session)
