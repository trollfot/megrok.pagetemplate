# -*- coding: utf-8 -*-

from grokcore.component import baseclass, implements
from zope.pagetemplate.interfaces import IPageTemplate


class ViewPageTemplate(object):
    implements(IPageTemplate)

    def __init__(self, template, view):
        self.view = view
        self.template = template
        self.macros = template._template.macros
    
    def __call__(self, *args, **kw):
        return self.template.render(self.view)

    def pt_edit(self, source, content_type):
        return self.template._template.pt_edit(source, content_type)

    def pt_errors(self, namespace):
        return self.template._template.pt_errors(namespace)

    def read(self):
        return self.template._template.read()


class PageTemplate(object):
    baseclass()

    def __call__(self, view, request):
        return ViewPageTemplate(self.template, view)
