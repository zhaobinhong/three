"""empty message

Revision ID: 64118c0e3799
Revises: 
Create Date: 2017-03-13 03:57:23.852043

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '64118c0e3799'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('goods',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('g_name', sa.String(), nullable=True),
    sa.Column('g_price', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_goods_id'), 'goods', ['id'], unique=False)
    op.create_table('reqlog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('req_id', sa.String(), nullable=True),
    sa.Column('datatime', sa.String(), nullable=True),
    sa.Column('cipher', sa.String(), nullable=True),
    sa.Column('clear', sa.String(), nullable=True),
    sa.Column('base', sa.String(), nullable=True),
    sa.Column('basejson', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_reqlog_id'), 'reqlog', ['id'], unique=False)
    op.create_table('sign',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('password', sa.String(), nullable=True),
    sa.Column('req_id', sa.String(), nullable=True),
    sa.Column('openid', sa.String(), nullable=True),
    sa.Column('appkey', sa.String(), nullable=True),
    sa.Column('is_ok', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('openid'),
    sa.UniqueConstraint('req_id')
    )
    op.create_index(op.f('ix_sign_id'), 'sign', ['id'], unique=False)
    op.create_table('orders',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('order_num', sa.String(), nullable=True),
    sa.Column('good_id', sa.Integer(), nullable=True),
    sa.Column('drawee', sa.String(), nullable=True),
    sa.Column('address', sa.String(), nullable=True),
    sa.Column('g_name', sa.String(), nullable=True),
    sa.Column('g_price', sa.String(), nullable=True),
    sa.Column('mobile', sa.String(), nullable=True),
    sa.Column('g_type', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['good_id'], ['goods.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('address'),
    sa.UniqueConstraint('order_num')
    )
    op.create_table('status',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('req_id', sa.String(), nullable=True),
    sa.Column('status', sa.Integer(), nullable=True),
    sa.Column('owner_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['owner_id'], ['sign.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_status_id'), 'status', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_status_id'), table_name='status')
    op.drop_table('status')
    op.drop_table('orders')
    op.drop_index(op.f('ix_sign_id'), table_name='sign')
    op.drop_table('sign')
    op.drop_index(op.f('ix_reqlog_id'), table_name='reqlog')
    op.drop_table('reqlog')
    op.drop_index(op.f('ix_goods_id'), table_name='goods')
    op.drop_table('goods')
    # ### end Alembic commands ###
