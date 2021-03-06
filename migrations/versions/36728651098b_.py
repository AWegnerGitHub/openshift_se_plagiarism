"""empty message

Revision ID: 36728651098b
Revises: 16b749a93455
Create Date: 2015-12-16 11:22:20.949000

"""

# revision identifiers, used by Alembic.
revision = '36728651098b'
down_revision = '16b749a93455'

from alembic import op
import sqlalchemy as sa
import models


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tags',
    sa.Column('id', models.CoerceUTF8(length=125), nullable=False),
    sa.Column('wiki_body', models.CoerceUTF8(length=65000), nullable=True),
    sa.Column('wiki_excerpt', models.CoerceUTF8(length=700), nullable=True),
    sa.Column('excerpt_creation', sa.DateTime(), nullable=False),
    sa.Column('body_creation', sa.DateTime(), nullable=False),
    sa.Column('last_check_date', sa.DateTime(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tags')
    ### end Alembic commands ###
