"""Add cart

Revision ID: 8755d04f0f56
Revises: 
Create Date: 2021-03-05 20:45:08.103453

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8755d04f0f56'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('seed',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=True),
    sa.Column('seed_type', sa.String(length=50), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_seed_name'), 'seed', ['name'], unique=True)
    op.create_index(op.f('ix_seed_price'), 'seed', ['price'], unique=False)
    op.create_index(op.f('ix_seed_quantity'), 'seed', ['quantity'], unique=False)
    op.create_index(op.f('ix_seed_seed_type'), 'seed', ['seed_type'], unique=False)
    op.create_table('shoe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('size', sa.Float(), nullable=True),
    sa.Column('brand', sa.String(length=80), nullable=True),
    sa.Column('model', sa.String(length=89), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_shoe_brand'), 'shoe', ['brand'], unique=False)
    op.create_index(op.f('ix_shoe_model'), 'shoe', ['model'], unique=True)
    op.create_index(op.f('ix_shoe_size'), 'shoe', ['size'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=50), nullable=True),
    sa.Column('email', sa.String(length=50), nullable=True),
    sa.Column('password_hash', sa.String(length=90), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    op.create_table('cart_item',
    sa.Column('seed_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['seed_id'], ['seed.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('seed_id', 'user_id')
    )
    op.create_index(op.f('ix_cart_item_quantity'), 'cart_item', ['quantity'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_cart_item_quantity'), table_name='cart_item')
    op.drop_table('cart_item')
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_shoe_size'), table_name='shoe')
    op.drop_index(op.f('ix_shoe_model'), table_name='shoe')
    op.drop_index(op.f('ix_shoe_brand'), table_name='shoe')
    op.drop_table('shoe')
    op.drop_index(op.f('ix_seed_seed_type'), table_name='seed')
    op.drop_index(op.f('ix_seed_quantity'), table_name='seed')
    op.drop_index(op.f('ix_seed_price'), table_name='seed')
    op.drop_index(op.f('ix_seed_name'), table_name='seed')
    op.drop_table('seed')
    # ### end Alembic commands ###
