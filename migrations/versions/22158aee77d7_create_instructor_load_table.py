"""create instructor_load table

Revision ID: 22158aee77d7
Revises: bb0e40372451
Create Date: 2023-12-10 19:43:38.170753

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '22158aee77d7'
down_revision = 'bb0e40372451'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('instructor_load',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('school_year', sa.String(length=64), nullable=False),
    sa.Column('start_time', sa.String(length=64), nullable=False),
    sa.Column('day', sa.String(length=64), nullable=False),
    sa.Column('end_time', sa.String(length=64), nullable=False),
    sa.Column('instructor_id', sa.Integer(), nullable=False),
    sa.Column('subject_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['instructor_id'], ['instructor.id'], ),
    sa.ForeignKeyConstraint(['subject_id'], ['subject.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('instructor_load')
    # ### end Alembic commands ###