#!/bin/sh

echo `date` >> /var/log/check.log

echo "Wait for next..." >> /var/log/check.log
sleep 61
echo "Release lock" >> /var/log/check.log
