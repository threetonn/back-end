"""Edit subscriptions

Revision ID: 0cda529708e9
Revises: f6b32d2fe266
Create Date: 2022-11-11 14:23:55.250301

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '0cda529708e9'
down_revision = 'f6b32d2fe266'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('subscriptionduration', sa.Column('discount', sa.Float(asdecimal=True), nullable=False))
    op.drop_column('subscriptionduration', 'name')
    op.drop_column('subscriptionduration', 'day_count')
    op.add_column('usersubscription', sa.Column('day_count', sa.Integer(), nullable=False))
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('usersubscription', 'day_count')
    op.add_column('subscriptionduration', sa.Column('day_count', sa.INTEGER(), autoincrement=False, nullable=False))
    op.add_column('subscriptionduration', sa.Column('name', sa.VARCHAR(length=45), autoincrement=False, nullable=False))
    op.drop_column('subscriptionduration', 'discount')
    # ### end Alembic commands ###
