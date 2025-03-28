"""add Department

Revision ID: 69e582b0d1a5
Revises: 67d02c72a15a
Create Date: 2025-03-25 13:24:24.787464

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '69e582b0d1a5'
down_revision = '67d02c72a15a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
