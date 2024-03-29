#
# @queries.py Copyright (c)
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

import requests
from decouple import config
from ariadne import convert_kwargs_to_snake_case

address = config('address')
ipv4 = config('IPV4')


@convert_kwargs_to_snake_case
def listPosts_resolver(obj, info):
    try:
        url = ipv4 + address + '/resource'
        response = requests.get(url)
        payload = {
            "success": True,
            "posts": response.json()
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def getPost_resolver(obj, info, id):
    try:
        url = ipv4 + address + '/resource/id/' + id
        response = requests.get(url)
        payload = {
            "success": True,
            "post": response.json()
        }

    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"Todo item matching id {id} not found"]
        }

    return payload


@convert_kwargs_to_snake_case
def getPost_resolver_name(obj, info, name):
    try:
        url = ipv4 + address + '/resource/name/' + name
        response = requests.get(url)
        payload = {
            "success": True,
            "post": response.json()
        }

    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"Todo item matching name {name} not found"]
        }

    return payload


def listPosts_resolver_person(obj, info):
    try:
        url = ipv4 + address + '/person'
        response = requests.get(url)
        payload = {
            "success": True,
            "posts": response.json()
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def getPost_resolver_person(obj, info, id):
    try:
        url = ipv4 + address + '/person/id/' + id
        response = requests.get(url)
        payload = {
            "success": True,
            "post": response.json()
        }

    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"Todo item matching id {id} not found"]
        }

    return payload


@convert_kwargs_to_snake_case
def getPost_resolver_name_person(obj, info, name):
    try:
        url = ipv4 + address + '/person/name/' + name
        response = requests.get(url)
        payload = {
            "success": True,
            "post": response.json()
        }

    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"Todo item matching name {name} not found"]
        }

    return payload


@convert_kwargs_to_snake_case
def listPosts_resolver_booking(obj, info):
    try:
        url = ipv4 + address + '/booking'
        response = requests.get(url)
        payload = {
            "success": True,
            "posts": response.json()
        }
    except Exception as error:
        payload = {
            "success": False,
            "errors": [str(error)]
        }
    return payload


@convert_kwargs_to_snake_case
def getPost_resolver_booking(obj, info, id):
    try:
        url = ipv4 + address + '/booking/id/' + id
        response = requests.get(url)
        payload = {
            "success": True,
            "post": response.json()
        }
    except AttributeError:  # todo not found
        payload = {
            "success": False,
            "errors": [f"Todo item matching id {id} not found"]
        }
    return payload
