import croniter
from datetime import datetime

# 定义一个函数来生成Crontab表达式的描述
def get_crontab_description(crontab_expression):
    cron = croniter.croniter(crontab_expression)

    # 将Crontab表达式的各个部分转换为描述
    minute = cron.get_next(datetime)
    hour = cron.get_next(datetime)
    day_of_month = cron.get_next(datetime)
    month = cron.get_next(datetime)
    day_of_week = cron.get_next(datetime)

    # 生成人类可读的描述
    cron_description = f"在每个月的第{day_of_month.day}天的{hour.hour}时{minute.minute}分，星期{day_of_week.weekday()}的{month.month}月"
    return cron_description

# 示例Crontab表达式
crontab_expression = "0 0 * * *"

# 调用函数并输出结果
description = get_crontab_description(crontab_expression)
print(description)
