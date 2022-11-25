#!/usr/bin/env python3

try:
    raise Exception("error message")
except Exception as e:
    print(str(e))
