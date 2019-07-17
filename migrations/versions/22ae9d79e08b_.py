"""empty message

Revision ID: 22ae9d79e08b
Revises: d130be7dec09
Create Date: 2019-07-16 23:46:47.851496

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22ae9d79e08b'
down_revision = 'd130be7dec09'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('attendance',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('start_date_attendence', sa.DateTime(), nullable=True),
    sa.Column('end_date_attendence', sa.DateTime(), nullable=True),
    sa.Column('specific_start_date_attendence', sa.DateTime(), nullable=True),
    sa.Column('specific_end_date_attendence', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('attendance')
    # ### end Alembic commands ###