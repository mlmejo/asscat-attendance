"""add year_level to student table

Revision ID: 1fd1c41a9eb6
Revises: 957f3789aab3
Create Date: 2023-12-10 17:56:28.370695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fd1c41a9eb6'
down_revision = '957f3789aab3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.add_column(sa.Column('year_level', sa.Enum('FIRST_YEAR', 'SECOND_YEAR', 'THIRD_YEAR', 'FOURTH_YEAR', name='yearlevelchoices'), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('student', schema=None) as batch_op:
        batch_op.drop_column('year_level')

    # ### end Alembic commands ###