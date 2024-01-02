#!/usr/bin/env python

import argparse
import boto3

# Parse command line arguments
parser = argparse.ArgumentParser(description='Retrieve AWS Cost and Usage')
parser.add_argument('--access_key', required=True, help='AWS Access Key ID')
parser.add_argument('--secret_key', required=True, help='AWS Secret Access Key')
args = parser.parse_args()

# Create a new client for the Cost Explorer service
client = boto3.client('ce',
                     aws_access_key_id=args.access_key,
                     aws_secret_access_key=args.secret_key)

# Define the time period for the report
start_date = '2022-01-01'
end_date = '2022-01-31'

# Define the granularity for the report
granularity = 'DAILY'

# Get the cost and usage report
response = client.get_cost_and_usage(
    TimePeriod={
        'Start': start_date,
        'End': end_date
    },
    Granularity=granularity,
    Metrics=["UnblendedCost", "UsageQuantity"],
    GroupBy=[{'Type': 'DIMENSION', 'Key': 'SERVICE'},]

)

# Print the report data
print(response['ResultsByTime'])
