#!/usr/bin/env python
import optparse
from subprocess import check_call

def main():
    p = optparse.OptionParser(usage='%prog [options]')
    (options, args) = p.parse_args()
    check_call(['./custom_rst2s5.py', './talk.txt', './index.html'])
    # check_call(['open', './index.html'])

if __name__ == '__main__':
    main()