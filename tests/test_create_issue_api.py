import random
import string

import allure

from src import rest_client, json_fixtures

project = "WEBINAR"
summary = "New API issue"
issuetype = "Task"
description = "Description of API issue"


@allure.tag("API")
def test_create_issue_api():
    response = rest_client.create_issue(
        json=json_fixtures.create_issue_json(project=project, summary=summary, issuetype=issuetype,
                                             description=description))
    assert response.status_code == 201


@allure.tag("API")
def test_create_issue_api_no_summary():
    missed_summary = None
    response = rest_client.create_issue(
        json=json_fixtures.create_issue_json(project=project, summary=missed_summary, issuetype=issuetype,
                                             description=description))
    assert response.status_code == 400
    assert response.json()['errors'] == {"summary": "Operation value must be a string"}


@allure.tag("API")
def test_create_issue_api_exceeded_summary():
    exceeded_summary = ''.join(random.choices(string.ascii_lowercase, k=256))
    response = rest_client.create_issue(
        json=json_fixtures.create_issue_json(project=project, summary=exceeded_summary, issuetype=issuetype,
                                             description=description))
    assert response.status_code == 400
    assert response.json()['errors'] == {"summary": "Summary must be less than 255 characters."}