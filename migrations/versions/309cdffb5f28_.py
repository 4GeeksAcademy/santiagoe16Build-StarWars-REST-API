"""empty message

Revision ID: 309cdffb5f28
Revises: 0032d2d203e4
Create Date: 2024-10-03 22:13:25.017539

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '309cdffb5f28'
down_revision = '0032d2d203e4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('planets',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=250), nullable=False),
    sa.Column('climate', sa.String(length=250), nullable=True),
    sa.Column('terrain', sa.String(length=250), nullable=True),
    sa.Column('population', sa.String(length=250), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('planets')
    # ### end Alembic commands ###
