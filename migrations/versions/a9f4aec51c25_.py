"""empty message

Revision ID: a9f4aec51c25
Revises: 7562545255ae
Create Date: 2018-10-06 08:58:07.949973

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'a9f4aec51c25'
down_revision = '7562545255ae'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('common_post',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=True),
    sa.Column('board_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.String(length=100), nullable=True),
    sa.ForeignKeyConstraint(['board_id'], ['board.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['front_user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('board', sa.Column('boardname', sa.String(length=20), nullable=False))
    op.drop_column('board', 'boardName')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('board', sa.Column('boardName', mysql.VARCHAR(length=20), nullable=False))
    op.drop_column('board', 'boardname')
    op.drop_table('common_post')
    # ### end Alembic commands ###
