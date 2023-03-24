# -*- coding: utf-8 -*-

import doctest
import unittest
from megrok.pagetemplate import tests


def make_test(dottedname):
    test = doctest.DocTestSuite(
        dottedname,
        optionflags=doctest.ELLIPSIS|doctest.NORMALIZE_WHITESPACE|doctest.REPORT_NDIFF|doctest.IGNORE_EXCEPTION_DETAIL)
    test.layer = tests.MegrokPagetemplateLayer(tests)
    return test


def test_suite():
    suite = unittest.TestSuite()
    readme = doctest.DocFileSuite(
        '../README.txt', globs={'__name__': 'megrok.pagetemplate'},
        optionflags=(doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS|doctest.REPORT_NDIFF|doctest.IGNORE_EXCEPTION_DETAIL))
    readme.layer = tests.MegrokPagetemplateLayer(tests)
    suite.addTest(readme)
    for name in ['registration', 'namedtemplates', 'notemplate']:
        dottedname = dottedname = 'megrok.pagetemplate.tests.%s' % name
        suite.addTest(make_test(dottedname))
    return suite
