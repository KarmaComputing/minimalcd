"""add principle table

Revision ID: 0e8204e179aa
Revises: 
Create Date: 2022-04-12 23:57:29.207354

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0e8204e179aa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('principle',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('principle', sa.String(length=128), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('principle')
    # ### end Alembic commands ###
