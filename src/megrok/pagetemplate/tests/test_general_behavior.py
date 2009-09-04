# -*- coding: utf-8 -*-

import doctest
import unittest

from zope import component
from zope.testing import module
from zope.testing import cleanup


def moduleSetUp(test):
    module.setUp(test, '__main__')


def moduleTearDown(test):   
    module.tearDown(test)
    cleanup.cleanUp()


def zopeSetUp(test):
    module.setUp(test, 'megrok.pagetemplate.tests')


def zopeTearDown(test):
    cleanup.cleanUp()


def test_suite():
    optionflags = doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
    globs = {}
    suite = unittest.TestSuite()
   
    suite.addTest(
        doctest.DocFileSuite(
            '../README.txt',
            optionflags=optionflags,
            setUp=moduleSetUp,
            tearDown=moduleTearDown,
            globs=globs)
        )
    return suite
