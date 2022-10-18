"""Add all tables

Revision ID: 9675c3457633
Revises: 
Create Date: 2022-10-14 20:56:59.148802

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9675c3457633'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('gender',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('gym',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=True),
    sa.Column('address', sa.String(length=45), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('subscriptionduration',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=False),
    sa.Column('day_count', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('workouttype',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('subscription',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=False),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('price', sa.Float(asdecimal=True), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('SubscriptionDuration_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['SubscriptionDuration_id'], ['subscriptionduration.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_subscription_SubscriptionDuration_id'), 'subscription', ['SubscriptionDuration_id'], unique=False)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=False),
    sa.Column('surname', sa.String(length=45), nullable=False),
    sa.Column('patronomic', sa.String(length=45), nullable=True),
    sa.Column('birthday', sa.DateTime(), nullable=False),
    sa.Column('email', sa.String(length=45), nullable=False),
    sa.Column('phonenumber', sa.String(length=45), nullable=False),
    sa.Column('password', sa.String(length=128), nullable=False),
    sa.Column('Gender_id', sa.Integer(), nullable=False),
    sa.Column('Role_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Gender_id'], ['gender.id'], ),
    sa.ForeignKeyConstraint(['Role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phonenumber')
    )
    op.create_index(op.f('ix_user_Gender_id'), 'user', ['Gender_id'], unique=False)
    op.create_index(op.f('ix_user_Role_id'), 'user', ['Role_id'], unique=False)
    op.create_table('usersubscription',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('date_of_purchase', sa.DateTime(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('User_id', sa.Integer(), nullable=False),
    sa.Column('Subscription_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Subscription_id'], ['subscription.id'], ),
    sa.ForeignKeyConstraint(['User_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_usersubscription_Subscription_id'), 'usersubscription', ['Subscription_id'], unique=False)
    op.create_index(op.f('ix_usersubscription_User_id'), 'usersubscription', ['User_id'], unique=False)
    op.create_table('workout',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=45), nullable=False),
    sa.Column('WorkoutType_id', sa.Integer(), nullable=False),
    sa.Column('Trainer', sa.Integer(), nullable=False),
    sa.Column('start_date', sa.DateTime(), nullable=False),
    sa.Column('end_date', sa.DateTime(), nullable=False),
    sa.Column('Gym_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Gym_id'], ['gym.id'], ),
    sa.ForeignKeyConstraint(['Trainer'], ['user.id'], ),
    sa.ForeignKeyConstraint(['WorkoutType_id'], ['workouttype.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_workout_Gym_id'), 'workout', ['Gym_id'], unique=False)
    op.create_index(op.f('ix_workout_Trainer'), 'workout', ['Trainer'], unique=False)
    op.create_index(op.f('ix_workout_WorkoutType_id'), 'workout', ['WorkoutType_id'], unique=False)
    op.create_table('workouttype_has_subscription',
    sa.Column('WorkoutType_id', sa.Integer(), nullable=False),
    sa.Column('Subscription_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['Subscription_id'], ['subscription.id'], ),
    sa.ForeignKeyConstraint(['WorkoutType_id'], ['workouttype.id'], ),
    sa.PrimaryKeyConstraint('WorkoutType_id', 'Subscription_id')
    )
    op.create_index(op.f('ix_workouttype_has_subscription_Subscription_id'), 'workouttype_has_subscription', ['Subscription_id'], unique=False)
    op.create_index(op.f('ix_workouttype_has_subscription_WorkoutType_id'), 'workouttype_has_subscription', ['WorkoutType_id'], unique=False)
    op.create_table('workout_has_user',
    sa.Column('Workout_id', sa.Integer(), nullable=False),
    sa.Column('User_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['User_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['Workout_id'], ['workout.id'], ),
    sa.PrimaryKeyConstraint('Workout_id', 'User_id')
    )
    op.create_index(op.f('ix_workout_has_user_User_id'), 'workout_has_user', ['User_id'], unique=False)
    op.create_index(op.f('ix_workout_has_user_Workout_id'), 'workout_has_user', ['Workout_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_workout_has_user_Workout_id'), table_name='workout_has_user')
    op.drop_index(op.f('ix_workout_has_user_User_id'), table_name='workout_has_user')
    op.drop_table('workout_has_user')
    op.drop_index(op.f('ix_workouttype_has_subscription_WorkoutType_id'), table_name='workouttype_has_subscription')
    op.drop_index(op.f('ix_workouttype_has_subscription_Subscription_id'), table_name='workouttype_has_subscription')
    op.drop_table('workouttype_has_subscription')
    op.drop_index(op.f('ix_workout_WorkoutType_id'), table_name='workout')
    op.drop_index(op.f('ix_workout_Trainer'), table_name='workout')
    op.drop_index(op.f('ix_workout_Gym_id'), table_name='workout')
    op.drop_table('workout')
    op.drop_index(op.f('ix_usersubscription_User_id'), table_name='usersubscription')
    op.drop_index(op.f('ix_usersubscription_Subscription_id'), table_name='usersubscription')
    op.drop_table('usersubscription')
    op.drop_index(op.f('ix_user_Role_id'), table_name='user')
    op.drop_index(op.f('ix_user_Gender_id'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_subscription_SubscriptionDuration_id'), table_name='subscription')
    op.drop_table('subscription')
    op.drop_table('workouttype')
    op.drop_table('subscriptionduration')
    op.drop_table('role')
    op.drop_table('gym')
    op.drop_table('gender')
    # ### end Alembic commands ###
