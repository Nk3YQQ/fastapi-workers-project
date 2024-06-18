from datetime import datetime

from pydantic import BaseModel as DeclarativeBaseModel

from pydantic import Field, ConfigDict
from typing_extensions import Annotated, Optional

str_30 = Annotated[str, Field(max_length=30)]
str_50 = Annotated[str, Field(max_length=50)]
str_100 = Annotated[str, Field(max_length=100)]
str_5 = Annotated[str, Field(max_length=5)]


class BaseModel(DeclarativeBaseModel):
    model_config = ConfigDict(from_attributes=True)


class EmployeeBase(BaseModel):
    employee_id: int


class EmployeeCreate(BaseModel):
    first_name: str_30
    last_name: str_30
    title: str_100
    birth_date: datetime
    notes: str


class EmployeeUpdatePut(BaseModel):
    first_name: str_30
    last_name: str_30
    title: str_100
    birth_date: datetime
    notes: str


class EmployeeUpdatePatch(BaseModel):
    first_name: Optional[str_30] = None
    last_name: Optional[str_30] = None
    title: Optional[str_100] = None
    birth_date: Optional[datetime] = None
    notes: Optional[str] = None


class Order(BaseModel):
    order_id: int


class OrderCreate(BaseModel):
    customer_id: str_5
    employee_id: int
    order_date: datetime
    ship_city: str_50


class OrderUpdatePut(BaseModel):
    customer_id: str_5
    employee_id: int
    order_date: datetime
    ship_city: str_50


class OrderUpdatePatch(BaseModel):
    customer_id: Optional[str_5] = None
    employee_id: Optional[int] = None
    order_date: Optional[datetime] = None
    ship_city: Optional[str_50] = None


class CustomerBase(BaseModel):
    customer_id: str_5


class CustomerCreate(CustomerBase):
    company_name: str_100
    contact_name: str_100


class CustomerUpdatePut(BaseModel):
    company_name: str_100
    contact_name: str_100


class CustomerUpdatePatch(BaseModel):
    company_name: Optional[str_100] = None
    contact_name: Optional[str_100] = None
