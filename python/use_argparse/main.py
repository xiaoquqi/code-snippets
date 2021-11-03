#!/usr/bin/env python

import sys

from init_argparse import parse_sys_args

def main():
    args = parse_sys_args(sys.argv)
    args.func(args)

if __name__ == "__main__":
    main()
