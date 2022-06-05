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
import requests
from ariadne import convert_kwargs_to_snake_case
from decouple import config


address = config('address')
ADDRESS_CONVERTER_SERVICE = config('ADDRESS_CONVERTER_SERVICE')
ADDRESS_MACHINE_SERVICE = config('ADDRESS_MACHINE_SERVICE')


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
def ocr_converter_resolver(obj, info, file: any, language: str, format: str, converter : str):
    path = os.path.join(r"saved_files/converter_service/uploads/", file.filename)
    file.save(path)
    url = ADDRESS_CONVERTER_SERVICE

    payload = {'language': language,
               'format': format,
               'convert': converter}
    files = [('file', (file.filename, open(path, 'rb'), 'application/octet-stream'))]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    payloads = {
        "success": True,
        "post": response.json()
    }
    return payloads


@convert_kwargs_to_snake_case
def iris_recognition_resolver(obj, info, file: any, percentage: float):
    path = os.path.join(r"saved_files/machine_service/uploads/", file.filename)
    file.save(path)
    url = ADDRESS_MACHINE_SERVICE + '/iris_recognition'
    payload = {'percentage': percentage}
    files = [('file', (file.filename, open(path, 'rb'), 'application/octet-stream'))]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    payloads = {
        "success": True,
        "post": response.json()
    }
    return payloads
