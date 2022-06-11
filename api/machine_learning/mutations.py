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


ADDRESS_MACHINE_SERVICE = config('ADDRESS_MACHINE_SERVICE')
ipv4 = config('IPV4')


@convert_kwargs_to_snake_case
def iris_recognition_resolver(obj, info, file: any, percentage: float):
    path = os.path.join(r"saved_files/machine_service/uploads/", file.filename)
    file.save(path)
    url = ipv4 + ADDRESS_MACHINE_SERVICE + '/iris_recognition'
    payload = {'percentage': percentage}
    files = [('file', (file.filename, open(path, 'rb'), 'application/octet-stream'))]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    payloads = {
        "success": True,
        "post": response.json()
    }
    return payloads


@convert_kwargs_to_snake_case
def iris_train_resolver(obj, info, zip: any):
    path = os.path.join(r"saved_files/machine_service/uploads/", zip.filename)
    zip.save(path)
    url = ADDRESS_MACHINE_SERVICE + '/iris_recognition_train'
    payload = {}
    files = [('zip', (zip.filename, open(path, 'rb'), 'application/octet-stream'))]
    headers = {}
    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    payloads = {
        "success": True,
        "post": response.json()
    }
    return payloads


@convert_kwargs_to_snake_case
def object_recognizer_resolver(obj, info, file: any, name: str, model: str, percentage: float):
    path = os.path.join(r"saved_files/machine_service/uploads/", file.filename)
    file.save(path)
    url = ADDRESS_MACHINE_SERVICE + '/object_recognizer'

    payload = {'name': name,
               'model': model,
               'percentage': percentage}
    files = [('file', (file.filename, open(path, 'rb'), 'application/octet-stream'))]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    payloads = {
        "success": True,
        "post": response.json()
    }
    print(payloads)
    return payloads


@convert_kwargs_to_snake_case
def vggface_recognition_resolver(obj, info, file: any, image: any):
    try:
        path = os.path.join(r"saved_files/machine_service/uploads/", file.filename)
        file.save(path)
        path_image = os.path.join(r"saved_files/machine_service/uploads/", image.filename)
        image.save(path_image)
        url = ADDRESS_MACHINE_SERVICE + "/vggface_search_person"

        payload = {}
        files = [('file', (file.filename, open(path, 'rb'), 'application/octet-stream')),
                 ('person', (image.filename, open(path_image, 'rb'), 'application/octet-stream'))]
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload, files=files)

        payloads = {
            "success": True,
            "post": str(response.json())
        }
    except ValueError:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }
    return payloads


@convert_kwargs_to_snake_case
def emotion_recognition_resolver(obj, info, file: any):
    path = os.path.join(r"saved_files/machine_service/uploads/", file.filename)
    file.save(path)
    url = ADDRESS_MACHINE_SERVICE + "/emotion"

    payload = {}
    files = [('file', (file.filename, open(path, 'rb'), 'application/octet-stream'))]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    payloads = {
        "success": True,
        "post": response.json()
    }
    return payloads
