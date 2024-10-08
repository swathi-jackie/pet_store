"""empty message

Revision ID: a9b7889376b8
Revises: 
Create Date: 2024-10-04 10:02:22.306421

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a9b7889376b8'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('product',
    sa.Column('product_name', sa.String(length=200), nullable=False),
    sa.Column('product_desc', sa.String(length=1000), nullable=False),
    sa.Column('product_img', sa.String(length=100), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('seller_name', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('product_name')
    )
    op.create_table('order',
    sa.Column('order_id', sa.String(length=50), nullable=False),
    sa.Column('ordered_on', sa.DateTime(), nullable=False),
    sa.Column('payment_mode', sa.String(length=50), nullable=False),
    sa.Column('purchaser', sa.String(length=200), nullable=True),
    sa.Column('product_name', sa.String(length=200), nullable=True),
    sa.ForeignKeyConstraint(['product_name'], ['product.product_name'], ),
    sa.PrimaryKeyConstraint('order_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('order')
    op.drop_table('product')
    # ### end Alembic commands ###