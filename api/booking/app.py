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

from ariadne import load_schema_from_path, make_executable_schema, snake_case_fallback_resolvers, ObjectType, upload_scalar
from api.booking.queries import listPosts_resolver, getPost_resolver, listPosts_resolver_person, \
    getPost_resolver_person, getPost_resolver_booking, listPosts_resolver_booking, \
    getPost_resolver_name_person, getPost_resolver_name
from api.booking.mutations import create_post_resolver, update_post_resolver, delete_post_resolver, \
    delete_post_resolver_booking, update_post_resolver_booking, create_post_resolver_booking, \
    delete_post_resolver_person, create_post_resolver_person, update_post_resolver_person

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

type_defs = load_schema_from_path("api/booking/schema.graphql")
schema_booking = make_executable_schema(
    type_defs, query, mutation, snake_case_fallback_resolvers, upload_scalar
)

query_mutation_booking = ['listPosts', 'getPost', "getPostName",
                          "listPostsPerson", "getPostPerson", "getPostNamePerson",
                          "listPostsBooking", "getPostBooking", "createPost",
                          "updatePost", "deletePost", "createBooking", "updateBooking",
                          "deleteBooking"]
