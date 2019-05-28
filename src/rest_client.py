import requests
import base64

base_url = 'https://jira.hillel.it'
issues = '/issues'
issue_part = '/rest/api/2/issue'


username_password_base64 = "U2VyZ2lpSWV2ZG9reW1vdjpTZXJnaWlJZXZkb2t5bW92"


def login(json: dict):
    return requests.post(url=base_url+login_endpoint, json=json)


def get_issues():
    headers = {'Authorization': "Basic " + username_password_base64,
               'Content-Type': "application/json"}
    return requests.get(url=base_url+issues, headers=headers)


def find_issue(issue_id: str):
    headers = {'Authorization': "Basic " + username_password_base64,
               'Content-Type': "application/json"}
    url = "{}{}/{}".format(base_url, issue_part, issue_id)
    return requests.get(url=url, headers=headers)


def create_issue(json: dict):
    headers = {'Authorization': "Basic " + username_password_base64,
               'Content-Type': "application/json"}
    return requests.post(url=base_url+issue_part, headers=headers, json=json)


def update_issue(issue_id: str, json: dict):
    headers = {'Authorization': "Basic " + username_password_base64,
               'Content-Type': "application/json"}
    url = "{}{}/{}".format(base_url, issue_part, issue_id)
    return requests.put(url=url, headers=headers, json=json)


def delete_issue(issue_id: str):
    headers = {'Authorization': "Basic " + username_password_base64}
    url = "{}{}/{}".format(base_url, issue_part, issue_id)
    return requests.delete(url=url, headers=headers)


