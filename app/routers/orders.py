from fastapi import APIRouter

from app.routers.base import BaseRouter
from app.schemas import OrderCreate, OrderUpdatePatch, OrderUpdatePut
from models.models import Order


class OrderRouter(BaseRouter):
    model = Order
    router = APIRouter()

    def __init__(self, session):
        super().__init__(session)

        self._urlpatterns = self.make_url_patterns("{order_id}")
        self.add_routers_from_list(self._urlpatterns)

    async def create(self, requested_data: OrderCreate):
        await super().create(requested_data)

        return {"status": 201, "data": requested_data}

    async def put(self, instance_id: int, requested_data: OrderUpdatePut):
        await super().put(instance_id, requested_data)

        data = self.check_for_null_values(requested_data)

        return {"status": 200, "data": data}

    async def patch(self, instance_id: int, requested_data: OrderUpdatePatch):
        await super().patch(instance_id, requested_data)

        data = self.check_for_null_values(requested_data)

        return {"status": 200, "data": data}

    async def delete(self, instance_id: int):
        await super().delete(instance_id)

        return {"status": 204}
