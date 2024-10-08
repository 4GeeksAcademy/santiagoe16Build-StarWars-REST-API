"""empty message

Revision ID: 368b669aeffa
Revises: 309cdffb5f28
Create Date: 2024-10-05 01:55:51.066874

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '368b669aeffa'
down_revision = '309cdffb5f28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('subscription_date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('subscription_date', postgresql.TIMESTAMP(), autoincrement=False, nullable=False))

    # ### end Alembic commands ###
