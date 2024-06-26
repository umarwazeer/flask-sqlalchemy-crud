"""Initial migration.

Revision ID: 559196947ea8
Revises: 4b63aa880d85
Create Date: 2023-05-02 14:08:53.745364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '559196947ea8'
down_revision = '4b63aa880d85'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.add_column(sa.Column('salary', sa.Integer(), nullable=False))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('employee', schema=None) as batch_op:
        batch_op.drop_column('salary')

    # ### end Alembic commands ###
