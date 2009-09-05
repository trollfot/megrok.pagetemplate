===================
megrok.pagetemplate
===================

Introduction
------------

`megrok.pagetemplate` is a thin Grok layer above zope.pagetemplate
package. It allows the developper to register IPageTemplate components
using grokked components. The syntax is meant to be very simple and
readable. `megrok.pagetemplate` only provides one component named
PageTemplate and uses the basic grokcore.view and grokcore.viewlet
directives : name, view, context, layer. To make it even simplier and
straightforward, it uses the grokcore.view template registry to
register the template files associated to the pagetemplate component.


Getting started
---------------

First, we import our dependencies:

  >>> import grokcore.view as view
  >>> import megrok.pagetemplate as pt
  >>> from grokcore.component.testing import grok, grok_component
  

A complete yet self-explanatory example
---------------------------------------

To get started with the code itself, let's explain the concept behind
the PageTemplate component. As it is usually implemented in most zope3
application, only one component is used in order to display an object
: the View. The View is a multi adapter, adapting the context and the
request and providing a rendering method (__call__, usually). If we
want to customize a View, we need to subclass it or to override it. In
both case, we end end up with a new View and, in the worse case, the
code (the logic) inside the View needs to be duplicated.

The PageTemplate allows you to interact at the rendering level. It's a
component implement IPageTemplate and is registered as a multi
adapter, adapting a View and a Layer (request type). This PageTemplate
can be named, for even more customization possibilities. 

Let's get a concrete example to get into the concept. First, we need a
context. Our usecase will be to provide different renderings for an
adorable animal : the Mammoth. First, let's create our mammoth and a
simple view that displays it.


  >>> from zope.component import getMultiAdapter
  >>> from zope.pagetemplate.interfaces import IPageTemplate

  >>> class Mammoth(view.Context):
  ...     """A furry pachyderm
  ...     """
  ...     nickname = u"Grokky" 


  >>> class MammothView(view.View):
  ...     """A view that display a mammoth
  ...     """
  ...	  view.context(Mammoth)
  ...
  ...	  def update(self):
  ...	      self.mammoth_name = u"My name is %s." % self.context.nickname
  ...
  ...	  def render(self):
  ...	      template = getMultiAdapter((self, self.request), IPageTemplate)
  ...	      return template()

  >>> grok_component('my_mammoth_view', MammothView)
  True

As we can see here, the View render method is a call to the
PageTemplate component. It will render the template found by the
registry lookup.


To be complete, here, we'll provide a IPageTemplate component :

  >>> class NakedMammoth(pt.PageTemplate):
  ...     """A mammoth shown in its simpliest apparel
  ...     """
  ...     pt.view(MammothView)
  ...     template = view.PageTemplate(
  ...        '<span tal:replace="view/mammoth_name" /> I am naked !'
  ...        )

  >>> grok_component('NakedMammoth', NakedMammoth)
  True

Now that our template is registered, we can try to summon the view and
to render it :

  >>> from zope.publisher.browser import TestRequest
  >>> request = TestRequest()
  >>> mammoth = Mammoth()

  >>> mv = getMultiAdapter((mammoth, request), name="mammothview")
  >>> print mv()
  My name is Grokky. I am naked !
  <BLANKLINE>
  

