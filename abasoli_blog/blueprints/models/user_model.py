from werkzeug.security import generate_password_hash, check_password_hash

from .base_model import db, BaseModel


class UserModel(BaseModel):
    name = db.Column(
        db.String(50),
        nullable=False,
    )

    username = db.Column(
        db.String(50),
        nullable=False,
        unique=True,
    )

    email = db.Column(
        db.String,
        nullable=False,
        unique=True,
    )

    password_hash = db.Column(
        db.String,
        nullable=False,
    )

    @property
    def password(self):
        raise AttributeError("User password cannot be accessed!")

    @password.setter
    def password(self, new_password):
        hashed_password = generate_password_hash(new_password)
        self.password_hash = hashed_password

    def is_password_valid(self, password_to_check):
        return check_password_hash(self.password_hash, password_to_check)

    def __repr__(self) -> str:
        return "<User %s>" % self.username
