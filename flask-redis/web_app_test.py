import requests
from web_app import app


def test_app(mocker):
    mock_requests = mocker.patch.object(requests, 'get')
    mock_response = mocker.Mock()
    mock_response.status_code = 200
    mock_response.text = 'Mocked Response'
    mock_requests.return_value = mock_response
    response = app.test_client().get('/')
    print('response code',response.status_code)
    assert response.status_code == 200