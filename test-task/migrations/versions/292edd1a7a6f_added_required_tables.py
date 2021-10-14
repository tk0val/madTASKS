"""Added required tables

Revision ID: 292edd1a7a6f
Revises: 
Create Date: 2021-10-14 22:37:22.425514

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '292edd1a7a6f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('patients',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_of_birth', sa.Date(), nullable=True),
    sa.Column('diagnoses', sa.PickleType(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('patients')
    # ### end Alembic commands ###
