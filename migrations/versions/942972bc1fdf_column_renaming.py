"""empty message

Revision ID: 942972bc1fdf
Revises: eb2f53922436
Create Date: 2021-01-09 19:15:34.740830

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '942972bc1fdf'
down_revision = 'eb2f53922436'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('link', sa.Column('generated_hash', sa.String(length=50), nullable=True))
    op.drop_column('link', 'generated_short_link')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('link', sa.Column('generated_short_link', mysql.VARCHAR(length=50), nullable=True))
    op.drop_column('link', 'generated_hash')
    # ### end Alembic commands ###
