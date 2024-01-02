import requests
from datetime import datetime, timedelta

# 替换为您的GitHub令牌
token = "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"

# 计算一个月前的日期
one_month_ago = datetime.now() - timedelta(days=30)
formatted_date = one_month_ago.strftime('%Y-%m-%d')

# 获取趋势排名
#url = f'https://api.github.com/search/repositories?q=created:>{formatted_date}&sort=stars&order=desc'
url = f'https://api.github.com/search/repositories?q=stars:>0+created:>{formatted_date}&sort=stars&order=desc'
headers = {'Authorization': f'token {token}'}
response = requests.get(url, headers=headers)

if response.status_code == 200:
    trending_repositories = response.json()['items']
    for repository in trending_repositories:
        print(repository['name'], repository['html_url'])
else:
    print(f'Failed to retrieve trending repositories. Status code: {response.status_code}')
