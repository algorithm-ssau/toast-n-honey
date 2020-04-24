"""customers table

Revision ID: e936b401baf4
Revises: 
Create Date: 2020-04-23 20:28:16.027670

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e936b401baf4'
down_revision = '315f0946de5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('customers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Name', sa.NVARCHAR(length=100), nullable=False),
    sa.Column('Phone', sa.NVARCHAR(length=10), nullable=False),
    sa.Column('Email', sa.NVARCHAR(length=100), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('customers')
    # ### end Alembic commands ###
