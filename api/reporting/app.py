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

from api import app
from ariadne import load_schema_from_path, make_executable_schema, snake_case_fallback_resolvers, \
    ObjectType, upload_scalar
from api.reporting.mutations import city_date_resolver, gender_date_resolver, age_gender_resolver, \
    country_date_resolver, model_type_resolver, state_gender_resolver
from flask_cors import CORS

CORS(app)
query = ObjectType("Query")
mutation = ObjectType("Mutation")

mutation.set_field("city_date", city_date_resolver)
mutation.set_field("gender_date", gender_date_resolver)
mutation.set_field("age_gender", age_gender_resolver)
mutation.set_field("country_date", country_date_resolver)
mutation.set_field("model_type", model_type_resolver)
mutation.set_field("state_gender", state_gender_resolver)

type_defs = load_schema_from_path("api/reporting/schema.graphql")
schema_reporting = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers, upload_scalar
)
query_mutation_reporting = ["city_date", "gender_date", "age_gender", "country_date",
                            "model_type", "state_gender"]
