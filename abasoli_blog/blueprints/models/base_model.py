from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.exc import SQLAlchemyError
from datetime import datetime
from datetime import timezone

from . import db


class BaseModel(db.Model):
    __abstract__ = True

    @declared_attr
    def __tablename__(cls):
        model_name = cls.__name__.replace("Model", "")
        plural_table_name = f"{model_name.lower()}s"
        return plural_table_name

    id = db.Column(
        db.Integer,
        primary_key=True,
    )

    created_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )

    updated_at = db.Column(
        db.DateTime(timezone=True),
        nullable=True,
    )

    def save(self, app_session, auto_commit=False):
        app_session.add(self)

        if auto_commit:
            try:
                app_session.commit()
            except SQLAlchemyError as error:
                app_session.rollback()
                raise error
