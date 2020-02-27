"""
Jira webook handler
"""
import json
from http import HTTPStatus

from logger import logger


def handle_webhook(request: dict, _context) -> dict:
    """
    Handle a Jira webhook notification

    :param request: the HTTP request dict
    :param _context: the AWS Lambda execution context (not used)
    :return: an HTTP response dict
    """
    # logger.debug("Got webhook request: %s", json.dumps(request, indent=2))
    event = json.loads(request["body"])
    logger.debug("Got webhook event: %s", json.dumps(event, indent=2))
    response = {
        "statusCode": HTTPStatus.ACCEPTED,
        "body": "OK",
        "headers": {
            "Content-Type": "text/plain"
        }
    }
    logger.debug("Returning response: %s", json.dumps(response, indent=2))
    return response
