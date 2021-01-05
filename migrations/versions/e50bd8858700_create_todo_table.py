"""Create todo table

Revision ID: e50bd8858700
Revises: 
Create Date: 2021-01-05 13:34:30.619009

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e50bd8858700'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table(
      "todos",
      sa.Column("id", sa.Integer, primary_key=True),
      sa.Column("title", sa.String),
      sa.Column("created_on", sa.DateTime(timezone=True), server_default=func.now()),
      sa.Column("modified_on", sa.DateTime(timezone=True), onupdate=func.now()),
      sa.Column("completed", sa.Boolean),
    )


def downgrade():
    op.drop_table('todos')
