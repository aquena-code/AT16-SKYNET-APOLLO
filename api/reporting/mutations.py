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
from decouple import config


ADDRESS_REPORTING_SERVICE = config('ADDRESS_REPORTING_SERVICE')


# methods for person
@convert_kwargs_to_snake_case
def city_date_resolver(obj, info, start_date, end_date):
    try:
        url = ADDRESS_REPORTING_SERVICE + '/search_report_fill_time_location'

        payload = {'start_date': start_date, 'end_date': end_date}
        files = None
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload,
                                    files=files)
        payloads = {
            "success": True,
            "post": response.json()
        }
    except ValueError:  # date format errors

        payloads = {

            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }

    return payloads


@convert_kwargs_to_snake_case
def gender_date_resolver(obj, info, open_time, close_time):
    try:
        url = ADDRESS_REPORTING_SERVICE + '/search_report_start_finish_time_person_gender'

        payload = {'open_time': open_time, 'close_time': close_time}
        files = None
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload,
                                    files=files)
        payloads = {
            "success": True,
            "post": response.json()
        }
    except ValueError:  # date format errors

        payloads = {

            "success": False,
            "errors": [f"Incorrect time format provided. Time should be in "
                       f"the format HH:MM:SS"]
        }

    return payloads


@convert_kwargs_to_snake_case
def age_gender_resolver(obj, info, person_age, person_gender):
    try:
        url = ADDRESS_REPORTING_SERVICE + '/search_report_age_gender'

        payload = {'person_age': person_age, 'person_gender': person_gender}
        files = None
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload,
                                    files=files)
        payloads = {
            "success": True,
            "post": response.json()
        }
    except ValueError:  # date format errors

        payloads = {

            "success": False,
            "errors": [f"Incorrect age"]
        }

    return payloads


@convert_kwargs_to_snake_case
def country_date_resolver(obj, info, start_date, end_date):
    try:
        url = ADDRESS_REPORTING_SERVICE + '/search_report_date_person_country'

        payload = {'start_date': start_date, 'end_date': end_date}
        files = None
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload,
                                    files=files)
        payloads = {
            "success": True,
            "post": response.json()
        }
    except ValueError:  # date format errors

        payloads = {

            "success": False,
            "errors": [f"Incorrect date format provided. Date should be in "
                       f"the format dd-mm-yyyy"]
        }

    return payloads


@convert_kwargs_to_snake_case
def model_type_resolver(obj, info, model: str, type: str):
    try:
        url = ADDRESS_REPORTING_SERVICE + '/search_report_model_type'

        payload = {'model': model, 'type': type}
        files = None
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload,
                                    files=files)
        payloads = {
            "success": True,
            "post": response.json()
        }
    except ValueError:  # date format errors

        payloads = {

            "success": False,
            "errors": [f"Incorrect model or type"]
        }

    return payloads


@convert_kwargs_to_snake_case
def state_gender_resolver(obj, info, state: str, person_gender: str):
    try:
        url = ADDRESS_REPORTING_SERVICE + '/search_report_state_person_gender'

        payload = {'state': state, 'person_gender': person_gender}
        files = None
        headers = {}

        response = requests.request("POST", url, headers=headers, data=payload,
                                    files=files)
        payloads = {
            "success": True,
            "post": response.json()
        }
    except ValueError:  # date format errors

        payloads = {

            "success": False,
            "errors": [f"Incorrect state or gender"]
        }

    return payloads
