from fastapi import FastAPI

from app.routers.customers import CustomerRouter
from app.routers.employees import EmployeeRouter
from app.routers.orders import OrderRouter
from app.settings import ENGINE
from models.session import Session

session = Session(ENGINE)

app = FastAPI(title='Worker app')

customer_router = CustomerRouter(session)
employee_router = EmployeeRouter(session)
order_router = OrderRouter(session)

app.include_router(customer_router.router, prefix="/customers", tags=["customers"])
app.include_router(employee_router.router, prefix="/employees", tags=["employees"])
app.include_router(order_router.router, prefix="/orders", tags=["orders"])
