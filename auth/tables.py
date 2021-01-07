from sqlalchemy import (
    Table, 
    Column, 
    Integer, 
    String, 
    DateTime,
    ForeignKey
)
from sqlalchemy.sql import func
from resources import metadata

users = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String),
    Column("password", String),
    Column("created_on", DateTime(timezone=True), server_default=func.now()),
)

