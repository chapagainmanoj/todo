from ariadne import (
    gql,
    make_executable_schema,
    ObjectType,
)
from .queries import resolve_users
from .mutations import resolve_login, resolve_signup

type_defs = gql("""
    type User {
        id: ID!
        username: String!
    }
    type UsersResult {
        success: Boolean!
        errors: [String]
        records: [User]
    }
    type AuthResult {
        success: Boolean!
        errors: [String]
        token: String
    }
    type Query {
        users: UsersResult!
    }
    type Mutation {
        login(username: String!, password: String!): AuthResult!
        signup(username: String!, password: String!): AuthResult!
    }
""" )

query = ObjectType("Query")

query.set_field("users", resolve_users)

mutation = ObjectType("Mutation")

mutation.set_field("login", resolve_login)
mutation.set_field("signup", resolve_signup)

schema = make_executable_schema(type_defs, query, mutation)
