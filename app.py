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

import json
from api import app,db
from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType, combine_multipart_data, upload_scalar
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api.queries import listPosts_resolver, getPost_resolver, listPosts_resolver_person, \
    getPost_resolver_person, getPost_resolver_booking, listPosts_resolver_booking, \
    getPost_resolver_name_person, getPost_resolver_name
from api.mutations import create_post_resolver, update_post_resolver, delete_post_resolver, \
    delete_post_resolver_booking, update_post_resolver_booking, create_post_resolver_booking, \
    delete_post_resolver_person, create_post_resolver_person, update_post_resolver_person, \
    ocr_converter_resolver, image_converter_resolver, metadata_converter_resolver, \
    translator_converter_resolver, waptxt_converter_resolver, video_converter_resolver, \
    audio_converter_resolver, iris_recognition_resolver
from flask_cors import CORS

CORS(app)
query = ObjectType("Query")
mutation = ObjectType("Mutation")

query.set_field("listPosts", listPosts_resolver)
query.set_field("getPost", getPost_resolver)
query.set_field("getPostName", getPost_resolver_name)

query.set_field("listPostsPerson", listPosts_resolver_person)
query.set_field("getPostPerson", getPost_resolver_person)
query.set_field("getPostNamePerson", getPost_resolver_name_person)

query.set_field("listPostsBooking", listPosts_resolver_booking)
query.set_field("getPostBooking", getPost_resolver_booking)

mutation.set_field("createPost", create_post_resolver)
mutation.set_field("updatePost", update_post_resolver)
mutation.set_field("deletePost", delete_post_resolver)

mutation.set_field("createPerson", create_post_resolver_person)
mutation.set_field("updatePerson", update_post_resolver_person)
mutation.set_field("deletePerson", delete_post_resolver_person)

mutation.set_field("createBooking", create_post_resolver_booking)
mutation.set_field("updateBooking", update_post_resolver_booking)
mutation.set_field("deleteBooking", delete_post_resolver_booking)

mutation.set_field("convert_ocr", ocr_converter_resolver)
mutation.set_field("convert_image", image_converter_resolver)
mutation.set_field("convert_metadata", metadata_converter_resolver)
mutation.set_field("convert_translator", translator_converter_resolver)
mutation.set_field("convert_waptxt", waptxt_converter_resolver)
mutation.set_field("convert_video", video_converter_resolver)
mutation.set_field("convert_audio", audio_converter_resolver)

mutation.set_field("iris_recognition", iris_recognition_resolver)



type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers, upload_scalar
)


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    if request.content_type.startswith("multipart/form-data"):
        data = combine_multipart_data(
            json.loads(request.form.get("operations")),
            json.loads(request.form.get("map")),
            dict(request.files)
        )
    else:
        data = request.get_json()

    success, result = graphql_sync(
        schema,
        data,
        context_value=request,
        debug=app.debug
    )

    status_code = 200 if success else 400
    return jsonify(result), status_code
