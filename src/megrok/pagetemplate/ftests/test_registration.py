"""
  >>> from zope.publisher.browser import TestRequest
  >>> request = TestRequest()

  >>> obj = MyView(MyContext(), request)
  >>> print obj()
  <span>Test !</span>
  <div>
    <strong>It works</strong>
  </div>
  <BLANKLINE>

  >>> template = getMultiAdapter((obj, request), IPageTemplate)
  >>> IPageTemplate.providedBy(template)
  True

  >>> print template.macros
  {u'a_simple_macro': ...

  >>> print template.read()
  <span></span>
  <div>
    <strong>It works</strong>
  </div>
  <BLANKLINE>
"""

import megrok.pagetemplate
import grokcore.view
import grokcore.viewlet 

from zope.component import getMultiAdapter
from zope.pagetemplate.interfaces import IPageTemplate
from megrok.pagetemplate.ftests import FunctionalLayer

grokcore.view.templatedir("templates")


class MyContext(grokcore.view.Context):
    """A context.
    """


class MyView(grokcore.view.View):
    """A very simple view.
    """
    grokcore.view.context(MyContext)

    def update(self):
        self.label = u"Test !"

    def render(self):
        template = getMultiAdapter((self, self.request), IPageTemplate)
        return template()


class MyTemplate(megrok.pagetemplate.PageTemplate):
    grokcore.viewlet.view(MyView)
    grokcore.view.template("test")


def test_suite():
    from zope.testing import doctest
    suite = doctest.DocTestSuite(
        optionflags=doctest.NORMALIZE_WHITESPACE|doctest.ELLIPSIS
        )
    suite.layer = FunctionalLayer
    return suite
