from datetime import datetime

from sqlalchemy import String, ForeignKey
from sqlalchemy.dialects.postgresql import TEXT
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing_extensions import Annotated

intpk = Annotated[int, mapped_column(primary_key=True, index=True, autoincrement=True)]
customer_pk = Annotated[str, mapped_column(String(5), primary_key=True)]

str_100 = Annotated[str, mapped_column(String(100), nullable=False)]
str_30 = Annotated[str, mapped_column(String(30), nullable=False)]
str_50 = Annotated[str, mapped_column(String(50), nullable=False)]

date = Annotated[datetime, mapped_column(nullable=False)]
text = Annotated[str, mapped_column(TEXT, nullable=False)]

customer_id = Annotated[int, mapped_column(ForeignKey("customers.id"))]
employee_id = Annotated[int, mapped_column(ForeignKey("employees.id"))]


class Base(DeclarativeBase):
    pass


class Employee(Base):
    __tablename__ = 'employees'
    id: Mapped[intpk]
    first_name: Mapped[str_30]
    last_name: Mapped[str_30]
    title: Mapped[str_100]
    birth_date: Mapped[date]
    notes: Mapped[text]

    orders = relationship("Order", back_populates="employee", cascade="all, delete-orphan")

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Order(Base):
    __tablename__ = 'orders'
    id: Mapped[intpk]
    customer_id: Mapped[customer_id]
    employee_id: Mapped[employee_id]
    order_date: Mapped[date]
    ship_city: Mapped[str_50]

    employee = relationship("Employee", back_populates="orders")
    customer = relationship("Customer", back_populates="orders")


class Customer(Base):
    __tablename__ = 'customers'
    id: Mapped[customer_pk]
    company_name: Mapped[str_100]
    contact_name: Mapped[str_100]

    orders = relationship("Order", back_populates="customer", cascade="all, delete-orphan")

    def __str__(self):
        return f'{self.company_name} - {self.contact_name}'
