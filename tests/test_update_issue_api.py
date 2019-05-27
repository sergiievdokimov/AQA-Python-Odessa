import allure

from src import rest_client, json_fixtures

UPDATED_SUMMARY = "Updated API summary"
UPDATED_DESCRIPTION = "Updated API description"
UPDATED_ISSUETYPE = "Bug"
UPDATED_PROJECT = "WEBINAR"


@allure.tag("API")
def test_update_issue_api(create_issue, json):
    issue_id = create_issue.json()["key"]
    response = rest_client.update_issue(issue_id=issue_id,
                                        json=json_fixtures.create_issue_json(project=UPDATED_PROJECT,
                                                                             summary=UPDATED_SUMMARY,
                                                                             description=UPDATED_DESCRIPTION,
                                                                             issuetype=UPDATED_ISSUETYPE))
    assert response.status_code == 204

    updated_issue = rest_client.find_issue(issue_id)
    fields = updated_issue.json()['fields']
    print(fields)

    project = fields['project']['key']
    assert project == UPDATED_PROJECT

    issuetype = fields['issuetype']['name']
    assert issuetype == UPDATED_ISSUETYPE

    summary = fields['summary']
    assert summary == UPDATED_SUMMARY

    description = fields['description']
    assert description == UPDATED_DESCRIPTION