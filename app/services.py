import json

from fastapi import HTTPException


def get_object_or_404(session, model, instance_id):
    instance = session.get(model, instance_id)
    if not instance:
        raise HTTPException(status_code=404, detail=f'{model.__class__} not found')
    return instance


def check_object_or_400(instance, instance_list, model):
    if instance in instance_list:
        raise HTTPException(status_code=400, detail=f'{model.__class__.__name__} is already registered')
    return instance


def open_and_read_json_file(filepath):
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)


def generate_data(data_list):
    for data in data_list:
        yield data


def add_routers_from_list(router, url_list: list[dict]):
    for url in url_list:
        path = url.get("path")
        view = url.get("view")
        method = url.get("method")

        router.add_api_route(path, view, methods=[method])
