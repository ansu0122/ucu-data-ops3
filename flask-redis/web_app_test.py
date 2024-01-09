import pytest
import os
from unittest.mock import patch, Mock
from web_app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

@patch('web_app.Redis')
def test_app(mock_redis, client):
    redis_instance = mock_redis.return_value
    redis_instance.get.return_value = b'5'

    response = client.get('/')
    assert response.default_status == 200

if __name__ == '__main__':
    pytest.main()