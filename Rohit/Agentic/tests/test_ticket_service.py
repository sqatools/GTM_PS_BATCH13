import pytest
from unittest.mock import patch
from services.ticket_service import create_ticket


@patch("services.ticket_service.requests.post")
def test_create_ticket_success(mock_post):
    mock_post.return_value.status_code = 201
    mock_post.return_value.json.return_value = {"id": 101}

    result = create_ticket("WiFi Installation")

    assert result["ticket_id"] == 101
    assert result["status"] == "Ticket Created Successfully"


@patch("services.ticket_service.requests.post")
def test_create_ticket_failure(mock_post):
    mock_post.return_value.status_code = 500

    result = create_ticket("WiFi Installation")

    assert result["status"] == "Ticket API Failed"


@patch("services.ticket_service.requests.post")
def test_create_ticket_exception(mock_post):
    mock_post.side_effect = Exception("Connection error")

    result = create_ticket("WiFi Installation")

    assert "Error" in result["status"]