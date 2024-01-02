#!/usr/bin/env python3

from aliyunsdbssopenapi.request.v20171214 import QueryCostDetailRequest

# 设置 access_key_id 和 access_key_secret
client = AcsClient(access_key_id, access_key_secret, region_id)

# 创建请求
request = QueryCostDetailRequest.QueryCostDetailRequest()

# 设置查询条件
request.set_accept_format('json')
request.set_ProductCode("ecs")
request.set_SubscriptionType("PayAsYouGo")
request.set_PageSize(100)

# 发送请求
response = client.do_action_with_exception(request)

# 解析结果
result = json.loads(response)

# 获取资源名称
for item in result["Data"]["CostDetail"]:
    print(item["ResourceName"])
