import pytest
import json


@pytest.fixture()
def test_webhook_request():
    """ Generates API GW POST event"""

    event = {
        "id": 2,
        "timestamp": 1525698237764,
        "issue": {
            "id": "99291",
            "self": "https://jira.atlassian.com/rest/api/2/issue/99291",
            "key": "JRA-20002",
            "fields": {
                "summary": "I feel the need for speed",
                "created": "2009-12-16T23:46:10.612-0600",
                "description": "Make the issue nav load 10x faster",
                "labels": ["UI", "dialogue", "move"],
                "priority": "Minor"
            }
        },
        "user": {
            "self": "https://jira.atlassian.com/rest/api/2/user?username=brollins",
            "name": "brollins",
            "key": "brollins",
            "emailAddress": "bryansemail at atlassian dot com",
            "avatarUrls": {
                "16x16": "https://jira.atlassian.com/secure/useravatar?size=small&avatarId=10605",
                "48x48": "https://jira.atlassian.com/secure/useravatar?avatarId=10605"
            },
            "displayName": "Bryan Rollins [Atlassian]",
            "active": "True"
        },
        "changelog": {
            "items": [
                {
                    "toString": "A new summary.",
                    "to": None,
                    "fromString": "What is going on here?????",
                    "from": None,
                    "fieldtype": "jira",
                    "field": "summary"
                },
                {
                    "toString": "New Feature",
                    "to": "2",
                    "fromString": "Improvement",
                    "from": "4",
                    "fieldtype": "jira",
                    "field": "issuetype"
                }
            ],
            "id": 10124
        },
        "comment": {
            "self": "https://jira.atlassian.com/rest/api/2/issue/10148/comment/252789",
            "id": "252789",
            "author": {
                "self": "https://jira.atlassian.com/rest/api/2/user?username=brollins",
                "name": "brollins",
                "emailAddress": "bryansemail@atlassian.com",
                "avatarUrls": {
                    "16x16": "https://jira.atlassian.com/secure/useravatar?size=small&avatarId=10605",
                    "48x48": "https://jira.atlassian.com/secure/useravatar?avatarId=10605"
                },
                "displayName": "Bryan Rollins [Atlassian]",
                "active": True
            },
            "body": "Just in time for AtlasCamp!",
            "updateAuthor": {
                "self": "https://jira.atlassian.com/rest/api/2/user?username=brollins",
                "name": "brollins",
                "emailAddress": "brollins@atlassian.com",
                "avatarUrls": {
                    "16x16": "https://jira.atlassian.com/secure/useravatar?size=small&avatarId=10605",
                    "48x48": "https://jira.atlassian.com/secure/useravatar?avatarId=10605"
                },
                "displayName": "Bryan Rollins [Atlassian]",
                "active": True
            },
            "created": "2011-06-07T10:31:26.805-0500",
            "updated": "2011-06-07T10:31:26.805-0500"
        },
        "webhookEvent": "jira:issue_updated"
    }

    return {
        "body": json.dumps(event, indent=2),
        "resource": "/{proxy+}",
        "requestContext": {
            "resourceId": "123456",
            "apiId": "1234567890",
            "resourcePath": "/{proxy+}",
            "httpMethod": "POST",
            "requestId": "c6af9ac6-7b61-11e6-9a41-93e8deadbeef",
            "accountId": "123456789012",
            "identity": {
                "apiKey": "",
                "userArn": "",
                "cognitoAuthenticationType": "",
                "caller": "",
                "userAgent": "Custom User Agent String",
                "user": "",
                "cognitoIdentityPoolId": "",
                "cognitoIdentityId": "",
                "cognitoAuthenticationProvider": "",
                "sourceIp": "127.0.0.1",
                "accountId": "",
            },
            "stage": "prod",
        },
        "headers": {
            "Via": "1.1 08f323deadbeefa7af34d5feb414ce27.cloudfront.net (CloudFront)",
            "Accept-Language": "en-US,en;q=0.8",
            "CloudFront-Is-Desktop-Viewer": "true",
            "CloudFront-Is-SmartTV-Viewer": "false",
            "CloudFront-Is-Mobile-Viewer": "false",
            "X-Forwarded-For": "127.0.0.1, 127.0.0.2",
            "CloudFront-Viewer-Country": "US",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            "Upgrade-Insecure-Requests": "1",
            "X-Forwarded-Port": "443",
            "Host": "1234567890.execute-api.us-east-1.amazonaws.com",
            "X-Forwarded-Proto": "https",
            "X-Amz-Cf-Id": "aaaaaaaaaae3VYQb9jd-nvCd-de396Uhbp027Y2JvkCPNLmGJHqlaA==",
            "CloudFront-Is-Tablet-Viewer": "false",
            "Cache-Control": "max-age=0",
            "User-Agent": "Custom User Agent String",
            "CloudFront-Forwarded-Proto": "https",
            "Accept-Encoding": "gzip, deflate, sdch",
        },
        "httpMethod": "POST",
        "path": "/update",
    }
