from cron_descriptor import get_description, ExpressionDescriptor
from cron_descriptor import Options, CasingTypeEnum, DescriptionTypeEnum, ExpressionDescriptor


print(get_description("* 2 3 * *"))

descriptor = ExpressionDescriptor(
    expression = "*/10 * * * *",
    casing_type = CasingTypeEnum.Sentence,
    use_24hour_time_format = True
)

print(descriptor.get_description())
print("{}".format(descriptor))
