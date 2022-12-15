"""Removendo campo name e adicionando first_name, last_name e full_name

Revision ID: 72a6fdc8f61a
Revises: 
Create Date: 2022-12-14 20:29:31.410432

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '72a6fdc8f61a'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_index(op.f('ix_models_brand_code'), 'models', ['brand_code'], unique=False)
    op.create_index(op.f('ix_parts_model_code'), 'parts', ['model_code'], unique=False)
    op.add_column('users', sa.Column('first_name', sa.String(length=255), nullable=False))
    op.add_column('users', sa.Column('last_name', sa.String(length=255), nullable=False))
    op.add_column('users', sa.Column('full_name', sa.String(length=255), nullable=False))
    op.drop_column('users', 'name')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('name', mysql.VARCHAR(length=255), nullable=False))
    op.drop_column('users', 'full_name')
    op.drop_column('users', 'last_name')
    op.drop_column('users', 'first_name')
    op.drop_index(op.f('ix_parts_model_code'), table_name='parts')
    op.drop_index(op.f('ix_models_brand_code'), table_name='models')
    # ### end Alembic commands ###