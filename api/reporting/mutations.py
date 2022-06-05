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
