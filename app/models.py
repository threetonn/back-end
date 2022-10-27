from sqlalchemy import Column, DateTime, Float, ForeignKey, Integer, String, Boolean, Table, Text
from sqlalchemy.orm import relationship
from .database import Base


metadata = Base.metadata


class Gender(Base):
    __tablename__ = 'gender'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False, unique=True)


class Gym(Base):
    __tablename__ = 'gym'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    address = Column(String(45))


class Role(Base):
    __tablename__ = 'role'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False, unique=True)


class Subscriptionduration(Base):
    __tablename__ = 'subscriptionduration'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    day_count = Column(Integer, nullable=False)


class Workouttype(Base):
    __tablename__ = 'workouttype'

    id = Column(Integer, primary_key=True)
    name = Column(String(45))
    description = Column(Text)


class Subscription(Base):
    __tablename__ = 'subscription'

    id = Column(Integer, primary_key=True)
    name = Column(String(45), nullable=False)
    description = Column(Text)
    price = Column(Float(asdecimal=True), nullable=False)
    is_active = Column(Boolean, nullable=False)
    SubscriptionDuration_id = Column(ForeignKey('subscriptionduration.id'), nullable=False, index=True)

    SubscriptionDuration = relationship('Subscriptionduration')
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
    password = Column(String(128), nullable=False)
    Gender_id = Column(ForeignKey('gender.id'), nullable=False, index=True)
    Role_id = Column(ForeignKey('role.id'), nullable=False, index=True)

    Gender = relationship('Gender')
    Role = relationship('Role')
    Workouts = relationship('Workout', secondary='workout_has_user')


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
