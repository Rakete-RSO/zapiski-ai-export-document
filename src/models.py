import enum
import uuid

from sqlalchemy import DateTime, Enum, ForeignKey
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy.sql import func

from .database import Base


class SubscriptionTier(enum.Enum):
    Basic = "Basic"
    Pro = "Pro"
    Premium = "Premium"


class User(Base):
    __tablename__ = "users"
    __allow_unmapped__ = True

    id: Mapped = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        index=True,
    )
    username: Mapped[str] = mapped_column(unique=True, index=True)
    email: Mapped[str] = mapped_column(unique=True, index=True)
    password: Mapped[str] = mapped_column()
    subscription_tier: Mapped[str] = mapped_column(
        Enum(SubscriptionTier), default=SubscriptionTier.Basic
    )
    subscribed_date: Mapped[DateTime] = mapped_column(DateTime, default=func.now())

    chats: Mapped[list["Chat"]] = relationship("Chat", back_populates="user")


class Chat(Base):
    __tablename__ = "chats"
    __allow_unmapped__ = True

    id: Mapped = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        index=True,
    )
    user_id: Mapped = mapped_column(ForeignKey("users.id"))
    created_at: Mapped[str] = mapped_column(default="now")
    name: Mapped[str] = mapped_column()

    user: Mapped["User"] = relationship("User", back_populates="chats")
    messages: Mapped[list["Message"]] = relationship("Message", back_populates="chat")


class Message(Base):
    __tablename__ = "messages"
    __allow_unmapped__ = True

    id: Mapped = mapped_column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        unique=True,
        index=True,
    )
    # base64-encoded image, together the previx "data:image/png;base64,"
    base64_image: Mapped[str] = mapped_column(default="")
    chat_id: Mapped = mapped_column(ForeignKey("chats.id"))
    content: Mapped[str] = mapped_column(nullable=True)
    created_at: Mapped[str] = mapped_column(default="now")
    role: Mapped[str] = mapped_column()  # "user", "assistant", "system"
    visible: Mapped[bool] = mapped_column()

    chat: Mapped["Chat"] = relationship("Chat", back_populates="messages")
