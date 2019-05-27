import allure

from src import rest_client


@allure.tag("API")
def test_get_valid_issue_api(create_issue, delete_issue):
    issue_id = create_issue.json()["key"]
    response = rest_client.find_issue(issue_id=issue_id)
    assert response.status_code == 200
    assert response.json()['fields']['summary'] == 'Summary fixture'
    assert response.json()['fields']['description'] == 'Description fixture'


@allure.tag("API")
def test_get_invalid_issue_api():
    issue_id = "invalid key"
    response = rest_client.find_issue(issue_id=issue_id)
    assert response.status_code == 404


@allure.tag("API")
def test_get_issues_list():
    response = rest_client.get_issues()
    assert response.status_code == 200