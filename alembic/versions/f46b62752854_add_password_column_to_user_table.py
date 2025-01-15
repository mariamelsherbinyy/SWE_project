"""Add password column to User table

Revision ID: f46b62752854
Revises: 
Create Date: 2025-01-15 03:34:16.527346

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'f46b62752854'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    # Add 'password' column to 'user' table
    op.add_column('user', sa.Column('password', sa.String(), nullable=True))

def downgrade():
    # Remove 'password' column from 'user' table
    op.drop_column('user', 'password')