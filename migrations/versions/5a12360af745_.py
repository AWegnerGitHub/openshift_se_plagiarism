"""empty message

Revision ID: 5a12360af745
Revises: None
Create Date: 2015-12-15 01:28:58.755000

"""

# revision identifiers, used by Alembic.
revision = '5a12360af745'
down_revision = None

from alembic import op
import sqlalchemy as sa
import models


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', models.CoerceUTF8(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    ### end Alembic commands ###
