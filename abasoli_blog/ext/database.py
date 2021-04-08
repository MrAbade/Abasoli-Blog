from flask import Flask
from flask_sqlalchemy import SQLAlchemy, BaseQuery, Model

from abasoli_blog.utils.singleton import SingletonMeta


class Database(SQLAlchemy, metaclass=SingletonMeta):
    def __init__(
        self,
        app=None,
        use_native_unicode=True,
        session_options=None,
        metadata=None,
        query_class=BaseQuery,
        model_class=Model,
        engine_options=None,
    ):
        super().__init__(
            app=app,
            use_native_unicode=use_native_unicode,
            session_options=session_options,
            metadata=metadata,
            query_class=query_class,
            model_class=model_class,
            engine_options=engine_options,
        )


def init_app(app: Flask, db: Database = Database()):
    db.init_app(app)
    app.db = db

    from abasoli_blog.blueprints.models.user_model import UserModel
