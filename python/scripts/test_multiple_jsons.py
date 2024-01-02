import json

# 假设你有一个包含JSON字符串的列表
json_strings = ['{"name": "Alice", "age": 25}', '{"name": "Bob", "city": "New York", "country": "USA"}']

# 初始化一个空的字典来存储合并后的JSON数据
merged_json = {}

# 遍历列表中的每个JSON字符串并解析它们，然后将其合并到 merged_json 中
for json_string in json_strings:
    json_data = json.loads(json_string)
    for key, value in json_data.items():
        if key in merged_json:
            # 如果键已存在于 merged_json 中，将新值与旧值连接起来
            merged_json[key] = f"{merged_json[key]}\n{value}"
        else:
            merged_json[key] = value

# 将合并后的JSON数据转换为字符串
merged_json_string = json.dumps(merged_json)

print(merged_json_string)

