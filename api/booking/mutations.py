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


import requests
from ariadne import convert_kwargs_to_snake_case
from api import db
from api.booking.models import Post, Person, PersonPut, BookingPut, BookingCreate
from decouple import config


address = config('address')
ipv4 = config('IPV4')


@convert_kwargs_to_snake_case
def create_post_resolver(obj, info, name, type, model, state):
    try:
        url = ipv4 + address + '/resource'
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
def update_post_resolver(obj, info, id_source, name, type, model, state):
    try:
        url = ipv4 + address + '/resource/' + id_source
        dates = {'resource_name': name,
                 'resource_type': type,
                 'resource_model': model,
                 'resource_state': state
                }

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
        url = ipv4 + address + '/resource/' + id_source
        response = requests.delete(url)

        payload = {"success": True,
                   "post": response.json()
                   }

    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }

    return payload


# methods for person
@convert_kwargs_to_snake_case
def create_post_resolver_person(obj, info, name, age, city, country, gender):
    try:
        url = ipv4 + address + '/person'

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
def update_post_resolver_person(obj, info, id_person, name, age, city, country, gender):
    try:
        url = ipv4 + address + '/person/' + id_person
        dates = {'person_city': city,
                 'person_age': age,
                 'person_country': country,
                 'person_full_name': name,
                 'person_gender': gender
                }
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
def delete_post_resolver_person(obj, info, id_person):
    try:
        url = ipv4 + address + '/person/' + id_person
        response = requests.delete(url)

        payload = {"success": True,
                   "post": response.json()
                   }

    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }

    return payload


@convert_kwargs_to_snake_case
def create_post_resolver_booking(obj, info, description, subject, person_id, resource_id, date,
                                 end_time, start_time, state, type):
    try:
        url = ipv4 + address + '/booking'
        post = BookingCreate(
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


@convert_kwargs_to_snake_case
def update_post_resolver_booking(obj, info, id_booking, description=None, subject=None,
                                 person_id=None, resource_id=None, date=None, end_time=None,
                                 start_time=None, state=None, type=None):
    try:
        url = ipv4 + address + '/booking/' + id_booking
        put = BookingPut(description, subject, person_id, resource_id, date, end_time, start_time,
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
        url = ipv4 + address + '/booking/' + id_booking
        response = requests.delete(url)

        payload = {"success": True,
                   "post": response.json()
                   }

    except AttributeError:
        payload = {
            "success": False,
            "errors": ["Not found"]
        }
    return payload
