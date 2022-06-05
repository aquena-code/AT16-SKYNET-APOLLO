#
# @app.py Copyright (c)
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

from api.booking.app import schema_booking, query_mutation_booking
from api.convertor.app import schema_convertor, query_mutation_convertor
from api.machine_learning.app import schema_machine, query_mutation_machine
from api.reporting.app import schema_reporting, query_mutation_reporting
import json
from ariadne import graphql_sync, combine_multipart_data
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify

from api import app
from flask_cors import CORS

CORS(app)
schema = schema_booking


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    global schema
    if request.content_type.startswith("multipart/form-data"):
        data = combine_multipart_data(
            json.loads(request.form.get("operations")),
            json.loads(request.form.get("map")),
            dict(request.files)
        )
        if '(' in data['query'].split()[4]:
            query_mutation = data['query'].split()[4][:-1]
        else:
            query_mutation = data['query'].split()[4]
    else:
        data = request.get_json()
        if '(' in data['query'].split()[3]:
            query_mutation = data['query'].split()[3].split('(')[0]
        else:
            query_mutation = data['query'].split()[3]
    if query_mutation in query_mutation_booking:
        schema = schema_booking
    elif query_mutation in query_mutation_machine:
        schema = schema_machine
    elif query_mutation in query_mutation_convertor:
        schema = schema_convertor
    elif query_mutation in query_mutation_reporting:
        schema = schema_reporting
    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code
