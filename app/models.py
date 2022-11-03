from sqlalchemy import Boolean, Column, DateTime, Float, ForeignKey, Integer, String, Table, Text, text
from sqlalchemy.orm import relationship
from .database import Base


metadata = Base.metadata


class Feature(Base):
    __tablename__ = 'features'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)

    Subscriptions = relationship('Subscription', secondary='subscription_has_features')


class Gender(Base):
    __tablename__ = 'gender'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False, unique=True)


class Gym(Base):
    __tablename__ = 'gym'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    address = Column(String(45), nullable=False)


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False, unique=True)


class Subscriptionduration(Base):
    __tablename__ = 'subscriptionduration'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    day_count = Column(Integer, nullable=False)
    price = Column(Float(asdecimal=True), nullable=False)


class Subscriptiontype(Base):
    __tablename__ = 'subscriptiontype'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    type = Column(String(45), nullable=False)


class Workouttype(Base):
    __tablename__ = 'workouttype'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    description = Column(Text, nullable=False)
    image = Column(String(), nullable=True)


class Subscription(Base):
    __tablename__ = 'subscription'

    id = Column(Integer, primary_key=True)
    description = Column(Text)
    is_active = Column(Boolean, nullable=False, server_default=text("'1'"))
    SubscriptionDuration_id = Column(ForeignKey('subscriptionduration.id'), nullable=False, index=True)
    SubscriptionType_id = Column(ForeignKey('subscriptiontype.id'), nullable=False, index=True)

    SubscriptionDuration = relationship('Subscriptionduration')
    SubscriptionType = relationship('Subscriptiontype')
    WorkoutTypes = relationship('Workouttype', secondary='workouttype_has_subscription')


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    surname = Column(String(45), nullable=False)
    patronymic = Column(String(45))
    birthday = Column(DateTime, nullable=False)
    email = Column(String(45), nullable=False, unique=True)
    phone = Column(String(45), nullable=False, unique=True)
    password = Column(String(256), nullable=False)
    Gender_id = Column(ForeignKey('gender.id'), nullable=False, index=True)
    Role_id = Column(ForeignKey('role.id'), nullable=False, index=True)
    image = Column(String(), nullable=True)
    bio = Column(Text, nullable=True)

    Gender = relationship('Gender')
    Role = relationship('Role')
    WorkoutTypes = relationship('Workouttype', secondary='user_has_workouttype')
    Workouts = relationship('Workout', secondary='workout_has_user')


t_subscription_has_features = Table(
    'subscription_has_features', metadata,
    Column('Subscription_id', ForeignKey('subscription.id'), primary_key=True, nullable=False, index=True),
    Column('Features_id', ForeignKey('features.id'), primary_key=True, nullable=False, index=True)
)


t_user_has_workouttype = Table(
    'user_has_workouttype', metadata,
    Column('User_id', ForeignKey('user.id'), primary_key=True, nullable=False, index=True),
    Column('WorkoutType_id', ForeignKey('workouttype.id'), primary_key=True, nullable=False, index=True)
)


class Usersubscription(Base):
    __tablename__ = 'usersubscription'

    id = Column(Integer, primary_key=True)
    date_of_purchase = Column(DateTime, nullable=False)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    User_id = Column(ForeignKey('user.id'), nullable=False, index=True)
    Subscription_id = Column(ForeignKey('subscription.id'), nullable=False, index=True)

    Subscription = relationship('Subscription')
    User = relationship('User')


class Workout(Base):
    __tablename__ = 'workout'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    WorkoutType_id = Column(ForeignKey('workouttype.id'), nullable=False, index=True)
    Trainer = Column(ForeignKey('user.id'), nullable=False, index=True)
    start_date = Column(DateTime, nullable=False)
    end_date = Column(DateTime, nullable=False)
    Gym_id = Column(ForeignKey('gym.id'), nullable=False, index=True)

    Gym = relationship('Gym')
    user = relationship('User')
    WorkoutType = relationship('Workouttype')


t_workouttype_has_subscription = Table(
    'workouttype_has_subscription', metadata,
    Column('WorkoutType_id', ForeignKey('workouttype.id'), primary_key=True, nullable=False, index=True),
    Column('Subscription_id', ForeignKey('subscription.id'), primary_key=True, nullable=False, index=True)
)


t_workout_has_user = Table(
    'workout_has_user', metadata,
    Column('Workout_id', ForeignKey('workout.id'), primary_key=True, nullable=False, index=True),
    Column('User_id', ForeignKey('user.id'), primary_key=True, nullable=False, index=True)
)
