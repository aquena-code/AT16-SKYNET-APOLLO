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


ADDRESS_CONVERTER_SERVICE = config('ADDRESS_CONVERTER_SERVICE')
ipv4 = config('IPV4')


@convert_kwargs_to_snake_case
def ocr_converter_resolver(obj, info, file: any, language: str, format: str, converter : str):
    path = os.path.join(r"saved_files/converter_service/uploads/", file.filename)
    file.save(path)
    url = ipv4 + ADDRESS_CONVERTER_SERVICE

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
def image_converter_resolver(obj, info, file: any, color: str, rotate: str, vertical_flip: str,
                             horizontal_flip: str, height: str, width: str, format: str,
                             convert: str):
    path = os.path.join(r"saved_files/converter_service/uploads/", file.filename)
    file.save(path)
    url = ADDRESS_CONVERTER_SERVICE

    payload = {'color': color,
               'rotate': rotate,
               'vertical_flip': vertical_flip,
               'horizontal_flip': horizontal_flip,
               'height': height,
               'width': width,
               'format': format,
               'convert': convert}
    files = [('file', (file.filename, open(path, 'rb'), 'application/octet-stream'))]
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
    url = ADDRESS_CONVERTER_SERVICE

    payload = {'format': format,
               'convert': convert}
    files = [('file', (file.filename, open(path, 'rb'), 'application/octet-stream'))]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    payloads = {
        "success": True,
        "post": response.json()
    }
    return payloads


@convert_kwargs_to_snake_case
def translator_converter_resolver(obj, info, file: any, language_in: str, language_out: str,
                                  format: str, convert: str):
    path = os.path.join(r"saved_files/converter_service/uploads/", file.filename)
    file.save(path)
    url = ADDRESS_CONVERTER_SERVICE

    payload = {'language_in': language_in,
               'language_out': language_out,
               'format': format,
               'convert': convert}
    files = [('file', (file.filename, open(path, 'rb'), 'application/octet-stream'))]
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
    url = ADDRESS_CONVERTER_SERVICE

    payload = {'format': format,
               'convert': convert,
               'language_in': language_in}
    files = [('file', (file.filename, open(path, 'rb'), 'application/octet-stream'))]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    payloads = {
        "success": True,
        "post": response.json()
    }
    return payloads


@convert_kwargs_to_snake_case
def video_converter_resolver(obj, info, file: any, frame: str, width: str, height: str, color: str,
                             format: str, convert: str):
    path = os.path.join(r"saved_files/converter_service/uploads/", file.filename)
    file.save(path)
    url = ADDRESS_CONVERTER_SERVICE

    payload = {'frame': frame,
               'width': width,
               'height': height,
               'color': color,
               'format': format,
               'convert': convert}
    files = [('file', (file.filename, open(path, 'rb'), 'application/octet-stream'))]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    payloads = {
        "success": True,
        "post": response.json()
    }
    return payloads


@convert_kwargs_to_snake_case
def audio_converter_resolver(obj, info, file: any, acodex: str, bitrate: str, sample_rate: str,
                             audio_channel: str, format: str, convert: str):
    path = os.path.join(r"saved_files/converter_service/uploads/", file.filename)
    file.save(path)
    url = ADDRESS_CONVERTER_SERVICE

    payload = {'frame': acodex,
               'width': bitrate,
               'height': sample_rate,
               'color': audio_channel,
               'format': format,
               'convert': convert}
    files = [('file', (file.filename, open(path, 'rb'), 'application/octet-stream'))]
    headers = {}

    response = requests.request("POST", url, headers=headers, data=payload, files=files)

    payloads = {
        "success": True,
        "post": response.json()
    }
    return payloads
