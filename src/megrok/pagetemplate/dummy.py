"""
  >>> megrok.pagetemplate.testing.grok(__name__) 

  >>> from zope.component import getMultiAdapter
  >>> from zope.publisher.browser import TestRequest
  >>> request = TestRequest()
  >>> obj = MyView(MyContext(), request)
  >>> template = getMultiAdapter((obj, request), IPageTemplate, name='toto')
  >>> IPageTemplate.providedBy(template)
"""

import megrok.pagetemplate
import grokcore.view as grok
from zope.pagetemplate.interfaces import IPageTemplate


class MyContext(grok.Context):
    """A context.
    """

class MyView(grok.View):
    """A very simple view.
    """
    grok.context(MyContext)
    
class MyTemplate(megrok.pagetemplate.PageTemplate):
    grok.name("toto")
    grok.context(MyView)
    grok.template("test")


def test_suite():
    from zope.testing import doctest
    suite = doctest.DocTestSuite(
        optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS
        )
    return suite
