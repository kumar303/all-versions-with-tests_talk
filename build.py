#!/usr/bin/env python
import optparse
from subprocess import check_call

def main():
    p = optparse.OptionParser(usage='%prog [options]')
    (options, args) = p.parse_args()
    check_call(['./custom_rst2s5.py', './talk.txt', './talk.html'])
    # check_call(['open', './talk.html'])

if __name__ == '__main__':
    main()