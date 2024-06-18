from pydantic import BaseModel

from app.services import get_object_or_404, check_object_or_400


class BaseRouter:
    model = None
    router = None

    def __init__(self, session):
        self.session = session

    def make_url_patterns(self, instance_id):
        return [
            {"path": "/", "view": self.create, "method": "POST"},
            {"path": "/", "view": self.read_all, "method": "GET"},
            {"path": f"/{instance_id}", "view": self.read_one, "method": "GET"},
            {"path": f"/{instance_id}", "view": self.put, "method": "PUT"},
            {"path": f"/{instance_id}", "view": self.patch, "method": "PATCH"},
            {"path": f"/{instance_id}", "view": self.delete, "method": "DELETE"}
        ]

    def add_routers_from_list(self, url_list: list[dict]):
        for url in url_list:
            path = url.get("path")
            view = url.get("view")
            method = url.get("method")

            self.router.add_api_route(path, view, methods=[method])

    @staticmethod
    def convert_model_to_dict(requested_data: BaseModel):
        return requested_data.dict()

    def check_for_null_values(self, requested_data: BaseModel):
        data = self.convert_model_to_dict(requested_data)

        return {key: value for key, value in data.items() if value is not None}

    async def get_object(self, instance_id: int | str):
        return get_object_or_404(self.session, self.model, instance_id)

    async def create(self, requested_data: BaseModel):
        data = self.convert_model_to_dict(requested_data)

        new_instance = self.model(**data)

        instance_list = await self.read_all()

        if isinstance(new_instance.id, int):
            new_instance.id = len(instance_list) + 1

        instance = check_object_or_400(new_instance, instance_list, self.model)

        self.session.create(instance)

    async def read_all(self):
        return self.session.all(self.model)

    async def read_one(self, instance_id: int | str):
        instance = await self.get_object(instance_id)

        return instance

    async def put(self, instance_id: int | str, requested_data: BaseModel):
        data = self.convert_model_to_dict(requested_data)

        instance = await self.get_object(instance_id)

        self.session.update(instance, data)

    async def patch(self, instance_id: int | str, requested_data: BaseModel):
        data = self.convert_model_to_dict(requested_data)

        instance = await self.get_object(instance_id)

        self.session.update(instance, data)

    async def delete(self, instance_id: int | str):
        instance = await self.get_object(instance_id)

        self.session.delete(instance)
