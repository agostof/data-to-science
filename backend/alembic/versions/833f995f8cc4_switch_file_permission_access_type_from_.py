"""switch file permission "access" type from varchar to bool and rename "is_public"

Revision ID: 833f995f8cc4
Revises: 072c3b0d1571
Create Date: 2024-01-06 00:17:57.263612

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '833f995f8cc4'
down_revision: str | None = '072c3b0d1571'
branch_labels: str | None = None
depends_on: str | None = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file_permissions', sa.Column('is_public', sa.Boolean(), nullable=False, server_default='f'))
    op.drop_column('file_permissions', 'access')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('file_permissions', sa.Column('access', postgresql.ENUM('UNRESTRICTED', 'RESTRICTED', name='access_type'), autoincrement=False, nullable=False))
    op.drop_column('file_permissions', 'is_public')
    # ### end Alembic commands ###