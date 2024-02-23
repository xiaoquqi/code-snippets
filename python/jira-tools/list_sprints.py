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

# Connect to Jira
jira = JIRA(server=jira_url, basic_auth=(username, password))

# 获取所有项目
#projects = jira.projects()
# List of project keys
project_keys = ["PRD", "PRJ", "BUG", "REQ"]  # Add more projects as needed

# 遍历所有项目
for project_key in project_keys:
    print(f"Project Key: {project_key}")

    # 获取项目关联的看板
    boards = jira.boards(projectKeyOrID=project_key)

    # 遍历项目关联的看板
    for board in boards:
        print(f"  Board ID: {board.id}, Board Name: {board.name}")

        if board.type == "scrum":
            # 获取看板关联的Sprints
            sprints = jira.sprints(board.id)

            # 遍历看板关联的Sprints
            for sprint in sprints:
                print(f"    Sprint ID: {sprint.id}, Sprint Name: {sprint.name}, Status: {sprint.state}")
