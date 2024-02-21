import requests
import pytest
from endpoints.create_object import CreateObject
from endpoints.get_object import GetObject
from endpoints.update_object import UpdateObject
from endpoints.delete_object import DeleteObject

payload = {
    "name": "Apple MacBook Pro 13",
    "data": {
        "year": 2024,
        "price": 1849.99,
        "CPU model": "Intel Core i7",
        "Hard disk size": "1 TB"
    }
}



def test_create_object():
    new_object_endpoint = CreateObject()
    new_object_endpoint.new_object(payload=payload)
    new_object_endpoint.check_responce_is_200()
    new_object_endpoint.check_name(payload['name'])


def test_get_object(obj_id):
    get_obj_endpoint = GetObject()
    get_obj_endpoint.get_by_id(obj_id)
    get_obj_endpoint.check_responce_is_200()
    get_obj_endpoint.check_by_id(obj_id)



def test_update_object(obj_id):
    update_obj_endpoint = UpdateObject()
    update_obj_endpoint.update_by_id(obj_id, payload)
    update_obj_endpoint.check_responce_is_200()
    update_obj_endpoint.check_by_name(payload['name'])


def test_delete_object(obj_id):
    delete_obj_endpoint = DeleteObject()
    delete_obj_endpoint.delete_by_id(obj_id)
    delete_obj_endpoint.check_responce_is_200()
    delete_obj_endpoint.get_by_id(obj_id)
    delete_obj_endpoint.check_responce_is_404()
