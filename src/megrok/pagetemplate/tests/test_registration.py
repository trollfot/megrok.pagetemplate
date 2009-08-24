"""
  >>> megrok.pagetemplate.testing.grok(__name__) 
  >>> from zope.component import getMultiAdapter
  >>> from zope.publisher.browser import TestRequest
  >>> request = TestRequest()
  >>> obj = MyView(MyContext(), request)
  >>> obj.render()
  u'yay !\n'
"""

import unittest
from megrok.pagetemplate.tests import FunctionalLayer
#from megrok.pagetemplate import PageTemplate
import grokcore.view as grok
from zope.component import getMultiAdapter
from zope.pagetemplate.interfaces import IPageTemplate
from megrok.pagetemplate.tests import FunctionalLayer

grok.templatedir("templates")


class MyContext(grok.Context):
    """A context.
    """

class MyView(grok.View):
    """A very simple view.
    """
    grok.context(MyContext)
    template = None

    def render(self):
        template = getMultiAdapter((self, self.request),
                                   IPageTemplate)
        return template.render(self)


#class MyTemplate(PageTemplate):
#    grok.context(MyView)
#    grok.template("test")


def test_suite():
    from zope.testing import doctest
    suite = doctest.DocTestSuite(
        optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS
        )
    suite.layer = FunctionalLayer
    return suite
