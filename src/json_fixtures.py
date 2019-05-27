def login_json(username: str, password: str):
    return {"username": username, "password": password}


def create_issue_json(summary: str, issuetype: str, description: str, project: str):
    json = {}
    json["fields"] = {"summary": summary,
                      "issuetype": {"name": issuetype},
                      "description": description,
                      "project": {"key": project},
                      }
    return json
