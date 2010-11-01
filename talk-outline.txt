=======================================================
Supporting All Versions of Python All The Time With Tox
=======================================================

If you maintain a module that targets multiple environments then this talk
will explain the modern tools and techniques needed to ensure that your module
works in all versions of Python. You probably already have a massive test
suite using a tool like nosetests, py.test, hand rolled unittest, or something
completely custom. Why not plug your test suite into tox, a command line
program, and set up some continuous integration (CI) to make sure every code
change executes tests in all versions of Python, including 2.4 through 2.7,
Jython, and 3.x? As part of showing you how this works, the presenter will
provide a succinct build / test strategy for maintaining a module in both 2.x
and 3.x. Ultimately, this talk aims to bridge the gap between Python 2 and 3
so that our vast ecosystem of third party libraries will live on in the world
of Python 3.

- count of PyPI packages
  - percentage that support Python 3
  - percentage that support Jython

- how to support all versions all the time (overview)
  - brief intro to automated tests
  - using tox
  - using tox + Hudson for CI

- automated testing tools
  - nosetests
  - py.test
  - unittest2
  - plugins

- using tox
  - http://codespeak.net/tox/
  - demo
  - explanation of tox.ini
  - substitution variables
  - customizing an env
  - build vs. test
  - virtualenv

- a test suite for Python 2 and 3
  - explanation of 2to3
  - tox recipe

- integrating tox into Hudson
  - brief intro to Hudson
  - using the matrix build with $TOXENV
  - e.g. http://hudson.testrun.org/job/nose-unstable/

- congratulations
  - you now know how to maintain a module in all major versions of Python using...
    - a test runner
    - tox
    - Hudson

