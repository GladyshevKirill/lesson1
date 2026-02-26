import uuid

import pytest
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DB_URL = "postgresql+psycopg2://postgres:666666@localhost:5432/shop_db"

engine = create_engine(DB_URL)
Session = sessionmaker(bind=engine)


@pytest.fixture()
def db():
    session = Session()
    transaction = session.begin()
    try:
        yield session
    finally:
        transaction.rollback()
        session.close()


def test_add_client(db):
    name = f"test-client-{uuid.uuid4().hex[:8]}"
    client_id = db.execute(
        text("INSERT INTO clients(name) VALUES (:name) RETURNING id"),
        {"name": name},
    ).scalar_one()

    saved_name = db.execute(
        text("SELECT name FROM clients WHERE id = :id"),
        {"id": client_id},
    ).scalar_one()

    assert saved_name == name


def test_update_client(db):
    name = f"test-client-{uuid.uuid4().hex[:8]}"
    client_id = db.execute(
        text("INSERT INTO clients(name) VALUES (:name) RETURNING id"),
        {"name": name},
    ).scalar_one()

    new_name = f"updated-client-{uuid.uuid4().hex[:8]}"
    db.execute(
        text("UPDATE clients SET name = :name WHERE id = :id"),
        {"name": new_name, "id": client_id},
    )

    saved_name = db.execute(
        text("SELECT name FROM clients WHERE id = :id"),
        {"id": client_id},
    ).scalar_one()

    assert saved_name == new_name


def test_delete_client(db):
    name = f"test-client-{uuid.uuid4().hex[:8]}"
    client_id = db.execute(
        text("INSERT INTO clients(name) VALUES (:name) RETURNING id"),
        {"name": name},
    ).scalar_one()

    db.execute(
        text("DELETE FROM clients WHERE id = :id"),
        {"id": client_id},
    )

    exists = db.execute(
        text("SELECT EXISTS(SELECT 1 FROM clients WHERE id = :id)"),
        {"id": client_id},
    ).scalar_one()

    assert exists is False