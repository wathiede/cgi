#!/usr/bin/env python
"""Simple CGI program."""

import cgi
import cgitb
import sys

cgitb.enable()


def main(args):
    cgi.test()


if __name__ == '__main__':
    main(sys.argv[1:])

