"""empty message

Revision ID: 1b08d21a8c1d
Revises: 
Create Date: 2020-11-25 19:26:40.254392

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b08d21a8c1d'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('code',
    sa.Column('code', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('code')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=80), nullable=False),
    sa.Column('password', sa.String(length=80), nullable=False),
    sa.Column('role', sa.Enum('Administrador', 'Empleado', 'Usuario'), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('room',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('coworking', sa.String(length=255), nullable=False),
    sa.Column('capacity', sa.Integer(), nullable=False),
    sa.Column('disinfection', sa.Integer(), nullable=True),
    sa.Column('ventilation', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(length=80), nullable=True),
    sa.ForeignKeyConstraint(['username'], ['user.username'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('room')
    op.drop_table('user')
    op.drop_table('code')
    # ### end Alembic commands ###
