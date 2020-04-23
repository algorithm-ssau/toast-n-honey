"""empty message

Revision ID: 315f0946de5b
Revises: 
Create Date: 2020-04-19 21:17:25.408236

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '315f0946de5b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('customerId', sa.Integer(), nullable=False),
    sa.Column('productId', sa.Integer(), nullable=False),
    sa.Column('optionId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customerId'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['optionId'], ['options.id'], ),
    sa.ForeignKeyConstraint(['productId'], ['products.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('orders')
    # ### end Alembic commands ###