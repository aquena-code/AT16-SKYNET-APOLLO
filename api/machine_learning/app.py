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

from ariadne import load_schema_from_path, make_executable_schema, snake_case_fallback_resolvers, \
                    ObjectType, upload_scalar
from api.machine_learning.mutations import iris_recognition_resolver, iris_train_resolver, \
                                        object_recognizer_resolver, vggface_recognition_resolver, \
                                        emotion_recognition_resolver
from flask_cors import CORS
from api import app


CORS(app)
query = ObjectType("Query")
mutation = ObjectType("Mutation")

mutation.set_field("iris_recognition", iris_recognition_resolver)
mutation.set_field("iris_train", iris_train_resolver)
mutation.set_field("object_recognizer", object_recognizer_resolver)
mutation.set_field("vggface_recognition", vggface_recognition_resolver)
mutation.set_field("emotion_recognition", emotion_recognition_resolver)

type_defs = load_schema_from_path("api/machine_learning/schema.graphql")
schema_machine = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers, upload_scalar
)
query_mutation_machine = ["iris_recognition", "iris_train", "object_recognizer",
                          "vggface_recognition", "emotion_recognition"]
