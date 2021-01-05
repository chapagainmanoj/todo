from sqlalchemy import (
    Table, 
    Column, 
    Integer, 
    String, 
    Boolean,
    DateTime,
)
from sqlalchemy.sql import func
from db import metadata

import pdb; pdb.set_trace()
todos = Table(
    "todos",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String),
    Column("created_on", DateTime(timezone=True), server_default=func.now()),
    Column("modified_on", DateTime(timezone=True), onupdate=func.now()),
    Column("completed", Boolean),
)