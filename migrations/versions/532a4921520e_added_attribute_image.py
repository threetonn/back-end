"""Added attribute image

Revision ID: 532a4921520e
Revises: 06e01583b871
Create Date: 2022-10-31 21:37:35.312950

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '532a4921520e'
down_revision = '06e01583b871'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('image', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'image')
    # ### end Alembic commands ###
