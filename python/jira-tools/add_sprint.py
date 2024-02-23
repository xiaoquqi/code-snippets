import os
import re
from jira import JIRA

# Jira instance URL
jira_url = os.environ.get("JIRA_URL", "")
if not jira_url:
    raise ValueError("JIRA_URL environment variable is not set.")

# Jira credentials
username = os.environ.get("JIRA_USERNAME", "")
password = os.environ.get("JIRA_PASSWORD", "")
if not username or not password:
    raise ValueError("JIRA_USERNAME or JIRA_PASSWORD environment variables are not set.")

version_pattern = re.compile(r'v(\d+\.\d+\.\d+)')

# Connect to Jira
jira = JIRA(server=jira_url, basic_auth=(username, password))

# 获取所有项目
#projects = jira.projects()
# List of project keys
project_keys = ["PRD", "BUG", "REQ"]  # Add more projects as needed

def get_active_sprint(boards):
    """Return Active Sprint object"""
    active_sprint = None
    for board in boards:
        if board.type == "scrum":
            sprints = jira.sprints(board.id)
            for sprint in sprints:
                if sprint.state == "active":
                    return sprint

def get_active_version_number(sprint_name):
    version_number = None
    match = version_pattern.search(sprint_name)
    if match:
        version_number = match.group(1)

    return version_number

def get_active_version(search_vesion_number):
    active_version = None
    versions = jira.project_versions(project_key)
    for version in versions:
        if search_vesion_number in version.name:
            active_version = version.name
            break

    return active_version

def get_sprint_field(project_key, active_sprint_name):
    """Found an existing issue to get sprint field"""

    # Found one existing issue in this sprint to get sprint field
    jql_query = f'project = "{project_key}" AND sprint = "{active_sprint_name}"'
    issues = jira.search_issues(jql_query, maxResults=1)
    if not issues:
        return None

    issue = issues[0]
    for field_key, field_value in issue.raw['fields'].items():
        if not(field_key and field_value):
            continue

        if 'customfield' in field_key.lower():
            if isinstance(field_value, list):
                print(f"Field Key: {field_key}, Field Value: {field_value}")
                first_item = field_value[0]
                if 'sprint' in first_item:
                    return field_key


# 遍历所有项目
for project_key in project_keys:
    print(f"Project Key: {project_key}")

    # 获取项目关联的看板
    boards = jira.boards(projectKeyOrID=project_key)

    active_sprint = get_active_sprint(boards)
    print(f"Active sprint {active_sprint.name}, id is {active_sprint.id}")
    active_version_number = get_active_version_number(active_sprint.name)
    active_version = get_active_version(active_version_number)
    print(f"Active version {active_version}")

    sprint_field_id = get_sprint_field(project_key, active_sprint.name)
    print(f"Sprint field: {sprint_field_id}")

    jql_query = f'project = "{project_key}" AND fixVersion = "{active_version}" AND sprint != "{active_sprint.name}"'
    print(jql_query)

    issues = jira.search_issues(jql_query)
    for issue in issues:
        print(f"Issue Key: {issue.key}, Summary: {issue.fields.summary}")
        issue.update(fields={sprint_field_id: active_sprint.id})
        print(f"Sprint updated successfully for issue {issue.key}")
