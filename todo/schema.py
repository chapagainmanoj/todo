from ariadne import QueryType, make_executable_schema
from ariadne.asgi import GraphQL

type_defs = """
    type Query {
        hello: String!
    }
"""

query = QueryType()

@query.field("hello")
def resolve_hello(*_):
    return "Hello world"

schema = make_executable_schema(type_defs, query)
hello_gql = GraphQL(schema, debug=True)