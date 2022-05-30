from api import app,db

from ariadne import load_schema_from_path, make_executable_schema, \
    graphql_sync, snake_case_fallback_resolvers, ObjectType, combine_multipart_data, upload_scalar
from ariadne.constants import PLAYGROUND_HTML
from flask import request, jsonify
from api.queries import listPosts_resolver, getPost_resolver, listPosts_resolver_person, getPost_resolver_person
from api.mutations import create_post_resolver, update_post_resolver, delete_post_resolver, \
    create_post_resolver_person, update_post_resolver_person, ocr_converter_resolver
import json
from flask_cors import CORS

CORS(app)
query = ObjectType("Query")
mutation = ObjectType("Mutation")

query.set_field("listPosts", listPosts_resolver)
query.set_field("getPost", getPost_resolver)

query.set_field("listPostsPerson", listPosts_resolver_person)
query.set_field("getPostPerson", getPost_resolver_person)

mutation.set_field("createPost", create_post_resolver)
mutation.set_field("updatePost", update_post_resolver)
mutation.set_field("deletePost", delete_post_resolver)

mutation.set_field("createPerson", create_post_resolver_person)
mutation.set_field("updatePerson", update_post_resolver_person)
mutation.set_field("convert_ocr", ocr_converter_resolver)

type_defs = load_schema_from_path("schema.graphql")
schema = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers, upload_scalar
)

@app.route("/graphql2", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql2", methods=["POST"])
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
