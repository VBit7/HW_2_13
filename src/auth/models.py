import sqlalchemy.orm as orm
import sqlalchemy as sqa

from datetime import datetime


class Base(orm.DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: orm.Mapped[int] = orm.mapped_column(primary_key=True)
    username: orm.Mapped[str] = orm.mapped_column(sqa.String(20), index=True)
    email: orm.Mapped[str] = orm.mapped_column(sqa.String(100), unique=True, nullable=False)
    hashed_password: orm.Mapped[str] = orm.mapped_column(sqa.String(250), nullable=False)
    avatar: orm.Mapped[str] = orm.mapped_column(sqa.String(250), nullable=True)
    refresh_token: orm.Mapped[str] = orm.mapped_column(sqa.String(250), nullable=True)
    is_active: orm.Mapped[bool] = orm.mapped_column(default=True)
    created_at: orm.Mapped[datetime] = orm.mapped_column(sqa.DateTime, default=sqa.func.now())
    updated_at: orm.Mapped[datetime] = orm.mapped_column(sqa.DateTime, default=sqa.func.now(), onupdate=sqa.func.now())