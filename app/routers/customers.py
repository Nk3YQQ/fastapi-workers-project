from fastapi import APIRouter

from models.models import Customer
from .base import BaseRouter
from ..schemas import CustomerCreate, CustomerUpdatePut, CustomerUpdatePatch


class CustomerRouter(BaseRouter):
    router = APIRouter()
    model = Customer

    def __init__(self, session):
        super().__init__(session)

        self._urlpatterns = self.make_url_patterns("{customer_id}")
        self.add_routers_from_list(self._urlpatterns)

    async def create(self, requested_data: CustomerCreate):
        await super().create(requested_data)

        return {"status": 201, "data": requested_data}

    async def put(self, instance_id: str, requested_data: CustomerUpdatePut):
        await super().put(instance_id, requested_data)

        data = self.check_for_null_values(requested_data)

        return {"status": 200, "data": data}

    async def patch(self, instance_id: str, requested_data: CustomerUpdatePatch):
        await super().patch(instance_id, requested_data)

        data = self.check_for_null_values(requested_data)

        return {"status": 200, "data": data}

    async def delete(self, instance_id: str):
        await super().delete(instance_id)

        return {"status": 204}
