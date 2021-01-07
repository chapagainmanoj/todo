from ariadne import (
    gql,
    make_executable_schema,
    ObjectType,
)

from .queries import resolve_todos, resolve_todo
from .mutations import resolve_create_todo, resolve_complete_todo, resolve_delete_todo

type_defs = gql("""
    type Todo {
        id: ID!
        title: String!
        completed: Boolean!
        created_on: String!
    }
    type TodoResult {
        success: Boolean!
        errors: [String]
        record: Todo
    }
    type TodosResult {
        success: Boolean!
        errors: [String]
        records: [Todo]
    }
    type DeleteTodoResult {
        success: Boolean!
        errors: [String]
    }
    type Query {
        todos: TodosResult!
        todo(todoId: ID!): TodoResult!
    }
    type Mutation {
        createTodo(title: String!): TodoResult!
        deleteTodo(todoId: ID!): DeleteTodoResult!
        completeTodo(todoId: String!): TodoResult!
    }
""")

query = ObjectType("Query")

query.set_field('todos', resolve_todos)
query.set_field('todo', resolve_todo)

mutation = ObjectType("Mutation")
mutation.set_field("createTodo", resolve_create_todo)
mutation.set_field("completeTodo", resolve_complete_todo)
mutation.set_field("deleteTodo", resolve_delete_todo)

schema = make_executable_schema(type_defs, query, mutation)

# mutation newTodo {
#   createTodo(title:"Complete todo app") {
#     success
#     errors
#     record {
#       id
#       completed
#       title
#     }
#   }
# }

# mutation completeTodo {
#   completeTodo(todoId: "1") {
#     success
#     errors
#     record { id completed title created_on }
#   }
# }

# query fetchAll {
#   todos {
#     success
#     errors
#     records {
#       id
#       completed
#       created_on
#       title
#     }
#   }
# }
