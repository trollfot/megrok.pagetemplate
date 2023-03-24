# -*- coding: utf-8 -*-

import grokcore.view
import martian
import zope.component
from grokcore.view.meta.views import TemplateGrokker
from zope.pagetemplate.interfaces import IPageTemplate
from zope.publisher.interfaces.browser import IDefaultBrowserLayer

from megrok.pagetemplate.components import PageTemplate


class PageTemplateTemplateGrokker(TemplateGrokker):
    martian.component(PageTemplate)

    def has_render(self, factory):
        return False

    def has_no_render(self, factory):
        return True


class PageTemplateGrokker(martian.ClassGrokker):
    martian.priority(990)
    martian.component(PageTemplate)
    martian.directive(grokcore.view.name)
    martian.directive(grokcore.view.view)
    martian.directive(grokcore.view.provides, default=IPageTemplate)
    martian.directive(grokcore.view.layer, default=IDefaultBrowserLayer)

    def grok(self, name, factory, module_info, **kw):
        factory.module_info = module_info
        return martian.ClassGrokker.grok(
            self, name, factory, module_info, **kw)

    def execute(self, factory, config, name, view, layer, provides, **kw):
        pagetemplate = factory()
        adapts = (view, layer)
        config.action(
            discriminator=('adapter', adapts, provides, name),
            callable=zope.component.provideAdapter,
            args=(pagetemplate, adapts, provides, name))

        return True
