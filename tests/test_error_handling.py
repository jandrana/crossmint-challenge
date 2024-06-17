import sys
import os
import pytest
import requests
import time

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from api_interactions import ApiClient, get_env_variable

def simulate_and_assert_error(api_client, mock_status_code=None, exception=None, expected_message=None, capsys=None):
    with pytest.MonkeyPatch.context() as m:
        def mock_get(*args, **kwargs):
            if exception:
                raise exception()
            else:
                response = requests.Response()
                response.status_code = mock_status_code
                raise requests.exceptions.HTTPError(response=response)
        
        m.setattr(requests, "get", mock_get)

        try:
            api_client.get_goal_map()
        except requests.exceptions.RequestException:
            pass

        if capsys and expected_message:
            captured = capsys.readouterr()
            assert expected_message in captured.out

def test_invalid_api_url_404(capsys):
    """Test case: invalid API URL"""
    candidate_id = get_env_variable('CANDIDATE_ID')
    invalid_url = "https://invalid_url/api/"

    api_client = ApiClient(invalid_url, candidate_id)
    expected_message = "404 Not found. The URL may be wrong. \n\tCheck the API_URL value in the .env file."

    simulate_and_assert_error(api_client, mock_status_code=404, expected_message=expected_message, capsys=capsys)

def test_invalid_candidate_id_500(capsys):
    """Test case: invalid candidate ID"""
    base_url = get_env_variable('API_URL')
    invalid_candidate_id = "invalid_candidate_id"

    api_client = ApiClient(base_url, invalid_candidate_id)
    expected_message = "500 Internal Server Error. \n\tCheck the CANDIDATE_ID value in the .env file."

    simulate_and_assert_error(api_client, mock_status_code=500, expected_message=expected_message, capsys=capsys)

def test_too_many_requests_429(capsys):
    """Test case: too many requests"""
    base_url = get_env_variable('API_URL')
    candidate_id = get_env_variable('CANDIDATE_ID')

    api_client = ApiClient(base_url, candidate_id)
    expected_message = "429 Too Many Requests. Wait before trying again."

    simulate_and_assert_error(api_client, mock_status_code=429, expected_message=expected_message, capsys=capsys)

def test_timeout(capsys):
    """Test case: request timeout"""
    base_url = get_env_variable('API_URL')
    candidate_id = get_env_variable('CANDIDATE_ID')

    api_client = ApiClient(base_url, candidate_id)
    expected_message = "The request timed out. Wait before trying again."

    simulate_and_assert_error(api_client, exception=requests.exceptions.Timeout, expected_message=expected_message, capsys=capsys)
