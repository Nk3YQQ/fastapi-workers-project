from app.settings import CUSTOMERS_DATA_PATH, EMPLOYEES_DATA_PATH, ORDERS_DATA_PATH
from commands.base import CommandHandler
from app.services import open_and_read_json_file, generate_data
from models.models import Customer, Employee, Order


class Fill(CommandHandler):
    model = None
    filepath = None

    def run(self, session):
        orders_data = open_and_read_json_file(self.filepath)
        generate_orders_data = list(generate_data(orders_data))

        for data in generate_orders_data:
            instance = self.model(**data)
            session.create(instance)


class CustomerFill(Fill):
    model = Customer
    filepath = CUSTOMERS_DATA_PATH


class EmployeeFill(Fill):
    model = Employee
    filepath = EMPLOYEES_DATA_PATH


class OrderFill(Fill):
    model = Order
    filepath = ORDERS_DATA_PATH
