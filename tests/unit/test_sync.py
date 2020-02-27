"""
Unit tests for sync methods
"""

from http import HTTPStatus
from jts import handler

from tests.unit.fixtures import *


def test_request_handler(test_webhook_request):
    response = handler.handle_webhook(test_webhook_request, None)
    assert response["statusCode"] == HTTPStatus.ACCEPTED
