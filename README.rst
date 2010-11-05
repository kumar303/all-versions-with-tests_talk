=======================================================
Supporting All Versions of Python All The Time With Tox
=======================================================

This talk explains the modern techniques that every module maintainer needs to
know in order to support all major versions of Python. You probably already
have a massive test suite using a tool like nosetests, py.test, hand rolled
unittest, etc. This talk will focus on using the tox command line tool to
build and run your tests in all versions of Python, including 2.4 - 2.7,
Jython, and 3.x

About This Talk
---------------

`Tox`_ is a new tool that lets you set up isolated `virtual environments`_ to
test your module's deployment and compatibility with all major versions of
Python. It's easy to install and is flexible enough that it probably already
supports your existing test suite. With one simple command you can execute
your test suite in each version of Python, you can build its documentation
with `Sphinx`_, and get a nice printout of the results. It has also been
designed from the ground up to integrate into continuous integration (CI)
tools like `Hudson`_.

.. _Tox: http://codespeak.net/tox/
.. _Hudson: http://hudson-ci.org/
.. _virtual environments: http://pypi.python.org/pypi/virtualenv
.. _Sphinx: http://sphinx.pocoo.org/

Why Does PyCon Need a Talk Like This?
-------------------------------------

There are thousands of interesting third party packages that make Python a
useful language. However, a lot of these packages do not work in emerging
environments like Jython and Python3 because it requires extra effort to test
for them. Tox single handedly may revolutionize the way developers go about
supporting all these environments at once. Usually, it only requires a few
minor changes to support these environments and with tox you can catch
problems early on. A talk like this is especially crucial as developers of
existing modules attempt to support both Python 2.x and Python 3.x.

Slide Outline
-------------

- count of PyPI packages

  - percentage that support Python 3
  - percentage that support Jython
  - let's fix that!

- how to support all versions all the time (overview)

  - common development pattern
  - how to use tox
  - how to use tox + Hudson for CI

- common development pattern
  
  - your test suite
    
    - nosetests
    - py.test
    - unittest2 ?
  
  - your dependencies
  - a virtualenv

- using tox

  - demo
  - explanation of tox.ini
  - substitution variables
  - customizing an env
  - build vs. test
  - virtualenv
  - Sphinx docs and other custom commands

- a test suite for Python 2 and 3

  - explanation of 2to3, distribute
  - tox recipe

- integrating tox into Hudson

  - brief intro to Hudson
  - bootstrapping a test slave
  - using the matrix build with $TOXENV
  - e.g. http://hudson.testrun.org/job/nose-unstable/

- congratulations

  - you now know how to maintain a module in all major versions of Python using...

    - a test runner
    - tox
    - Hudson

