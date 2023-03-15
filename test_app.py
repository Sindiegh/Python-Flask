import pytest
from flask.testing import FlaskClient
from flask import Flask, url_for
from app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_home(client: FlaskClient):
    response = client.get('/')
    assert response.status_code ==200
    assert b"search" in response.data