import os
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

# Source and target project keys
source_project_key = "REQ"
target_project_key = "PRD"

# Connect to Jira
jira = JIRA(server=jira_url, basic_auth=(username, password))

# Get components from the source project
source_components = jira.project_components(source_project_key)

# Create components in the target project
for component in source_components:
    print(component)
    new_component = {
        'project': target_project_key,
        'name': component.name,
        'description': component.description() if hasattr(component, 'description') else "",
        'leadUserName': component.lead.name if component.lead else None,
        'assigneeType': component.assigneeType,
        'isAssigneeTypeValid': component.isAssigneeTypeValid
    }

    try:
        jira.create_component(**new_component)
        print(f"Component '{component.name}' copied successfully.")
    except Exception as e:
        print(f"Failed to copy component '{component.name}'. Error: {e}")
