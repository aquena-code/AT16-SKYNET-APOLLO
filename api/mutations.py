#
# @mutations.py Copyright (c)
# 2643 Av  Melchor Perez de Olguin, Colquiri Sud, Cochabamba, Bolivia.
# 1376 Av General Inofuentes esquina calle 20, La Paz, Bolivia.
# All rights reserved.
#
# This software is the confidential and proprietary information of
# Jalasoft, ("Condidential Information"). You shall # not
# disclose such Confidential Information and shall use it only in
# accordance with the terms of the license agreement you entered into
# with Jalasoft .
#

import os.path

from ariadne import convert_kwargs_to_snake_case

from api import db
from api.models import Post, Person
from decouple import config
address = config('address')
import requests


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
def ocr_converter_resolver(obj, info, file: any, language: str, format: str, converter : str):
    path = os.path.join(r"saved_files/converter_service/uploads/", file.filename)
    file.save(path)
    url = "http://127.0.0.1:5003/convert"

    payload = {'language': language,
               'format': format,
               'convert': converter}
    files = [
        ('file', (file.filename, open(path, 'rb'),
                  'application/octet-stream'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    payloads = {
        "success": True,
        "post": response.json()
    }
    return payloads

@convert_kwargs_to_snake_case
def image_converter_resolver(obj, info, file: any, color: str, rotate: str, vertical_flip: str, horizontal_flip: str,
                             height: str, width: str, format: str, convert: str):
    path = os.path.join(r"saved_files/converter_service/uploads/", file.filename)
    file.save(path)
    url = "http://127.0.0.1:5003/convert"

    payload = {'color': color,
               'rotate': rotate,
               'vertical_flip': vertical_flip,
               'horizontal_flip': horizontal_flip,
               'height': height,
               'width': width,
               'format': format,
               'convert': convert}
    files = [
        ('file', (file.filename, open(path, 'rb'),
                  'application/octet-stream'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    payloads = {
        "success": True,
        "post": response.json()
    }
    return payloads

@convert_kwargs_to_snake_case
def metadata_converter_resolver(obj, info, file: any, format: str, convert: str):
    path = os.path.join(r"saved_files/converter_service/uploads/", file.filename)
    file.save(path)
    url = "http://127.0.0.1:5003/convert"

    payload = {'format': format,
               'convert': convert}
    files = [
        ('file', (file.filename, open(path, 'rb'),
                  'application/octet-stream'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    payloads = {
        "success": True,
        "post": response.json()
    }
    return payloads

@convert_kwargs_to_snake_case
def translator_converter_resolver(obj, info, file: any, language_in: str, language_out: str, format: str, convert: str):
    path = os.path.join(r"saved_files/converter_service/uploads/", file.filename)
    file.save(path)
    url = "http://127.0.0.1:5003/convert"

    payload = {'language_in': language_in,
               'language_out': language_out,
               'format': format,
               'convert': convert}
    files = [
        ('file', (file.filename, open(path, 'rb'),
                  'application/octet-stream'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    payloads = {
        "success": True,
        "post": response.json()
    }
    return payloads

@convert_kwargs_to_snake_case
def waptxt_converter_resolver(obj, info, file: any, format: str, convert: str, language_in: str):
    path = os.path.join(r"saved_files/converter_service/uploads/", file.filename)
    file.save(path)
    url = "http://127.0.0.1:5003/convert"

    payload = {'format': format,
               'convert': convert,
               'language_in': language_in}
    files = [
        ('file', (file.filename, open(path, 'rb'),
                  'application/octet-stream'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    payloads = {
        "success": True,
        "post": response.json()
    }
    return payloads

@convert_kwargs_to_snake_case
def video_converter_resolver(obj, info, file: any, frame: str, width: str, height: str, color: str, format: str, convert: str):
    path = os.path.join(r"saved_files/converter_service/uploads/", file.filename)
    file.save(path)
    url = "http://127.0.0.1:5003/convert"

    payload = {'frame': frame,
               'width': width,
               'height': height,
               'color': color,
               'format': format,
               'convert': convert}
    files = [
        ('file', (file.filename, open(path, 'rb'),
                  'application/octet-stream'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    payloads = {
        "success": True,
        "post": response.json()
    }
    return payloads

@convert_kwargs_to_snake_case
def audio_converter_resolver(obj, info, file: any, acodex: str, bitrate: str, sample_rate: str, audio_channel: str,
                             format: str, convert: str):
    path = os.path.join(r"saved_files/converter_service/uploads/", file.filename)
    file.save(path)
    url = "http://127.0.0.1:5003/convert"

    payload = {'frame': acodex,
               'width': bitrate,
               'height': sample_rate,
               'color': audio_channel,
               'format': format,
               'convert': convert}
    files = [
        ('file', (file.filename, open(path, 'rb'),
                  'application/octet-stream'))
    ]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    payloads = {
        "success": True,
        "post": response.json()
    }
    return payloads