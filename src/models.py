from enum import Enum as PyEnum

from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Enum as SqlEnum

db = SQLAlchemy()


class UserRole(PyEnum):
    user = "user"
    support = "support"
    admin = "admin"


class BlogStatus(PyEnum):
    draft = "draft"
    unpublished = "unpublished"
    published = "published"


class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(120), nullable=False)
    email_id = db.Column(db.String(180), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(SqlEnum(UserRole), default=UserRole.user, nullable=False)

    is_active = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )

    blogs = db.relationship("Blog", backref="author", lazy=True)

    def __repr__(self):
        return f"<User {self.fullname}>"


class Blog(db.Model):
    __tablename__ = "blogs"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(300), nullable=False)
    body = db.Column(db.Text, nullable=False)
    status = db.Column(SqlEnum(BlogStatus), default=BlogStatus.draft, nullable=False)

    is_active = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    updated_at = db.Column(
        db.DateTime,
        default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp(),
    )

    created_by = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)

    def __repr__(self):
        return f"<Blog {self.title[:20]}>"


def init_create_table(app):
    with app.app_context():
        db.create_all()
        print("Database tables created successfully!")
