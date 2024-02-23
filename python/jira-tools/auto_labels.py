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

# List of project keys
project_keys = ["PRD", "PRJ", "BUG", "REQ"]  # Add more projects as needed

# Connect to Jira
jira = JIRA(server=jira_url, basic_auth=(username, password))

# Iterate over each project
for project_key in project_keys:
    print(f"Processing issues in project: {project_key}")

    # Get all issues in the specified project
    project_issues = jira.search_issues(f'project={project_key}', maxResults=False)

    # Print and update labels for each issue
    for issue in project_issues:
        print(f"Issue Key: {issue.key}")
        print(f"Summary: {issue.fields.summary}")
        print(f"Description: {issue.fields.description}")

        pattern = r'\[(.*?)\]'
        matches = re.findall(pattern, issue.fields.summary)

        # Extract labels from the issue title
        title_labels = [label.replace(" ", "-") for label in matches]

        # Get existing labels
        existing_labels = issue.fields.labels

        # Add new labels if not already present
        for label in title_labels:
            if label not in existing_labels:
                print(f"Add label {label}")
                existing_labels.append(label)

        # Update the issue with the modified labels
        issue.update(fields={"labels": existing_labels})
        print(f"Labels updated for issue {issue.key}: {existing_labels}")
        print("--------------")
