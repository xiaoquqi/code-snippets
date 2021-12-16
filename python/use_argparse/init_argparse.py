#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Common modules for parse script arguments"""

import argparse
import logging
import sys

def parse_sys_args(argv):
    """Parses commaond-line arguments"""
    parser = argparse.ArgumentParser(
        description="Demo for argparse")
    parser.add_argument(
        "-d", "--debug", action="store_true", dest="debug",
        default=False, help="Enable debug message.")
    parser.add_argument(
        "-v", "--verbose", action="store_true", dest="verbose",
        default=False, help="Show message in standard output.")

    subparsers = parser.add_subparsers(title="Avaliable commands")

    # Subparsers
    parser_sub = subparsers.add_parser("subtest")
    parser_sub.add_argument(
        "-a", "--arg1", dest="arg1", required=True,
        help="Demo for subparsers argument1")
    parser_sub.add_argument(
        "--arg2", dest="arg2", required=True,
        help="Demo for subparsers argument1")
    parser_sub.set_defaults(func=test_parser_sub)

    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    else:
        return parser.parse_args(argv[1:])

def test_parser_sub(args):
    logging.info("arg1 is %s" % args.arg1)
    logging.debug("arg2 is %s" % args.arg2)
