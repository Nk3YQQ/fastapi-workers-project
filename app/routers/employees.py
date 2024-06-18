from fastapi import APIRouter

from app.routers.base import BaseRouter
from app.schemas import EmployeeCreate, EmployeeUpdatePut, EmployeeUpdatePatch
from models.models import Employee


class EmployeeRouter(BaseRouter):
    model = Employee
    router = APIRouter()

    def __init__(self, session):
        super().__init__(session)

        self._urlpatterns = self.make_url_patterns("{employee_id}")
        self.add_routers_from_list(self._urlpatterns)

    async def create(self, requested_data: EmployeeCreate):
        await super().create(requested_data)

        return {"status": 201, "data": requested_data}

    async def put(self, instance_id: int, requested_data: EmployeeUpdatePut):
        await super().put(instance_id, requested_data)

        data = self.check_for_null_values(requested_data)

        return {"status": 200, "data": data}

    async def patch(self, instance_id: int, requested_data: EmployeeUpdatePatch):
        await super().patch(instance_id, requested_data)

        data = self.check_for_null_values(requested_data)

        return {"status": 200, "data": data}

    async def delete(self, instance_id: int):
        await super().delete(instance_id)

        return {"status": 204}
