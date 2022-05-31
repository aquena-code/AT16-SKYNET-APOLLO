import os.path
import requests
from datetime import date

from ariadne import convert_kwargs_to_snake_case

from api import db
from api.models import Post, Person, Person_put, Booking_put, Booking_create
from decouple import config
address = config('address')


@convert_kwargs_to_snake_case
def create_post_resolver(obj, info, name, type, model, state):
    try:
        url = address + '/resource'
        post = Post(
            resource_name=name,
            resource_type=type,
            resource_model=model,
            resource_state=state
        )
        response = requests.post(url, json=post.to_dict())
        payload = {

            "success": True,
            "post": response.json()
        }
    except ValueError:  # date format errors

        payload = {

            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }

    return payload


@convert_kwargs_to_snake_case
def update_post_resolver(obj, info, id_source, name):
    try:
        url = address + '/resource/' + id_source
        dates = {'resource_name': name}

        response = requests.put(url, json=dates)
        payload = {
            "success": True,
            "post": response.json()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }

    return payload


@convert_kwargs_to_snake_case
def delete_post_resolver(obj, info, id_source):
    try:
        url = address + '/resource/' + id_source
        response = requests.delete(url)

        payload = {"success": True,
                   "post": response.json()
                   }

    except AttributeError:
        print(db)
        payload = {
            "success": False,
            "errors": ["Not found"]
        }

    return payload

# methods for person
@convert_kwargs_to_snake_case
def create_post_resolver_person(obj, info, name, age, city, country, gender):
    try:
        url = address + '/person'

        post = Person(
            person_age=age,
            person_city = city,
            person_country = country,
            person_full_name = name,
            person_gender = gender
        )
        response = requests.post(url, json=post.to_dict())
        payload = {

            "success": True,
            "post": response.json()
        }
    except ValueError:  # date format errors

        payload = {

            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }

    return payload


@convert_kwargs_to_snake_case
def update_post_resolver_person(obj, info, id_person, city):
    try:
        url = address + '/person/' + id_person
        dates = {'person_city': city}
        response = requests.put(url, json=dates)
        payload = {
            "success": True,
            "post": response.json()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }

    return payload


@convert_kwargs_to_snake_case
def update_post_resolver_person(obj, info, id_person, age=None, city=None, country=None, name=None,
                                gender=None):
    try:
        url = address + '/person/' + id_person
        put = Person_put(age, city, country, name, gender)
        response = requests.put(url, json=put.to_dict())
        payload = {
            "success": True,
            "post": response.json()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }
    return payload


@convert_kwargs_to_snake_case
def ocr_converter_resolver(obj, info, file: any, language: str, format: str, converter : str):
    path = os.path.join(r"saved_files/converter_service/uploads/", file.filename)
    file.save(path)
    url = "http://127.0.0.1:5003/convert"

    payload = {'language': 'eng',
               'format': 'docx',
               'convert': 'OCR'}
    files = [
        ('file', (file.filename, open(path, 'rb'),
                  'application/octet-stream'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    print(response.text)

    payloads = {
        "success": True,
        "post": response.json()
    }
    return payloads

@convert_kwargs_to_snake_case
def delete_post_resolver_person(obj, info, id_person):
    try:
        url = address + '/person/' + id_person
        response = requests.delete(url)

        payload = {"success": True,
                   "post": response.json()
                   }

    except AttributeError:
        print(db)
        payload = {
            "success": False,
            "errors": ["Not found"]
        }

    return payload


@convert_kwargs_to_snake_case
def create_post_resolver_booking(obj, info, description, subject, person_id, resource_id, date,
                                 end_time, start_time, state, type):
    try:
        url = address + '/booking'
        print(date)
        print("entrada bookin create")
        post = Booking_create(
            description=description,
            subject=subject,
            person_id=person_id,
            resource_id=resource_id,
            date=date,
            end_time=end_time,
            start_time=start_time,
            state=state,
            type=type
        )
        response = requests.post(url, json=post.to_dict())
        payload = {

            "success": True,
            "post": response.json()
        }
    except ValueError:  # date format errors

        payload = {

            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }

    return payload


def update_post_resolver_booking(obj, info, id_booking, description=None, subject=None,
                                 person_id=None, resource_id=None, date=None, end_time=None,
                                 start_time=None, state=None, type=None):
    try:
        url = address + '/booking/' + id_booking
        put = Booking_put(description, subject, person_id, resource_id, date, end_time, start_time,
                          state, type)
        response = requests.put(url, json=put.to_dict())
        payload = {
            "success": True,
            "post": response.json()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": ["item matching id {id} not found"]
        }
    return payload


@convert_kwargs_to_snake_case
def delete_post_resolver_booking(obj, info, id_booking):
    try:
        url = address + '/booking/' + id_booking
        response = requests.delete(url)

        payload = {"success": True,
                   "post": response.json()
                   }

    except AttributeError:
        print(db)
        payload = {
            "success": False,
            "errors": ["Not found"]
        }

    return payload
