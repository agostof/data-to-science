"""add vector layer and data product metadata tables

Revision ID: a50a73e16072
Revises: 671e0126bd17
Create Date: 2024-06-03 13:09:16.774389

"""
from alembic import op
import sqlalchemy as sa
from geoalchemy2 import Geometry
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'a50a73e16072'
down_revision: str | None = '671e0126bd17'
branch_labels: str | None = None
depends_on: str | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_geospatial_table('vector_layers',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('layer_name', sa.String(length=128), nullable=False),
    sa.Column('layer_id', sa.String(length=12), nullable=False),
    sa.Column('geom', Geometry(spatial_index=False, from_text='ST_GeomFromEWKT', name='geometry', nullable=False), nullable=False),
    sa.Column('properties', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('project_id', sa.UUID(), nullable=False),
    sa.Column('flight_id', sa.UUID(), nullable=True),
    sa.Column('data_product_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['data_product_id'], ['data_products.id'], ),
    sa.ForeignKeyConstraint(['flight_id'], ['flights.id'], ),
    sa.ForeignKeyConstraint(['project_id'], ['projects.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_geospatial_index('idx_vector_layers_geom', 'vector_layers', ['geom'], unique=False, postgresql_using='gist', postgresql_ops={})
    op.create_table('data_product_metadata',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('category', sa.String(length=16), nullable=False),
    sa.Column('properties', postgresql.JSONB(astext_type=sa.Text()), nullable=False),
    sa.Column('data_product_id', sa.UUID(), nullable=False),
    sa.Column('vector_layer_id', sa.UUID(), nullable=True),
    sa.ForeignKeyConstraint(['data_product_id'], ['data_products.id'], ),
    sa.ForeignKeyConstraint(['vector_layer_id'], ['vector_layers.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data_product_metadata')
    op.drop_geospatial_index('idx_vector_layers_geom', table_name='vector_layers', postgresql_using='gist', column_name='geom')
    op.drop_geospatial_table('vector_layers')
    # ### end Alembic commands ###
