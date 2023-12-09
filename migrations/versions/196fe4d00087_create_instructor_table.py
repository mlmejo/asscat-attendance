"""create instructor table

Revision ID: 196fe4d00087
Revises: f05362e024b3
Create Date: 2023-12-09 19:07:03.811163

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '196fe4d00087'
down_revision = 'f05362e024b3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('instructor',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=False),
    sa.Column('last_name', sa.String(length=64), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('is_instructor', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('is_instructor')

    op.drop_table('instructor')
    # ### end Alembic commands ###