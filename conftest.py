import pytest

from src import rest_client
from src import json_fixtures
from users_data import ValidUser


@pytest.fixture(scope="session")
def json():
    return json_fixtures


@pytest.fixture(scope="session")
def client():
    return rest_client


# @pytest.fixture(scope='session')
# def login(client, json):
#     json = client.login(json.login_json(ValidUser.username, ValidUser.password)).json()['session']
#     return json['value']


@pytest.fixture(scope="function")
def create_issue():
    project = 'WEBINAR'
    summary = 'Summary fixture'
    description = 'Description fixture'
    issuetype = 'Task'

    response = rest_client.create_issue(json_fixtures.create_issue_json(project=project, summary=summary, issuetype=issuetype, description=description))
    return response


@pytest.fixture(scope="function")
def delete_issue(create_issue):
    yield delete_issue
    rest_client.delete_issue(issue_id=create_issue.json()['id'])
