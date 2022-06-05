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
from ariadne import load_schema_from_path, make_executable_schema, \
    snake_case_fallback_resolvers, ObjectType, upload_scalar
from api.convertor.mutations import ocr_converter_resolver, image_converter_resolver, metadata_converter_resolver, \
    translator_converter_resolver, waptxt_converter_resolver, video_converter_resolver, \
    audio_converter_resolver
from flask_cors import CORS

CORS(app)
query = ObjectType("Query")
mutation = ObjectType("Mutation")

mutation.set_field("convert_ocr", ocr_converter_resolver)
mutation.set_field("convert_image", image_converter_resolver)
mutation.set_field("convert_metadata", metadata_converter_resolver)
mutation.set_field("convert_translator", translator_converter_resolver)
mutation.set_field("convert_waptxt", waptxt_converter_resolver)
mutation.set_field("convert_video", video_converter_resolver)
mutation.set_field("convert_audio", audio_converter_resolver)

type_defs = load_schema_from_path("api/convertor/schema.graphql")
# schema_convertor = make_executable_schema(
#     type_defs, query, mutation, snake_case_fallback_resolvers, upload_scalar
# )
schema_convertor = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers, upload_scalar
)
query_mutation_convertor = ["convert_ocr", "convert_image", "convert_metadata",
                            "convert_translator", "convert_waptxt", "convert_video",
                            "convert_audio"]
