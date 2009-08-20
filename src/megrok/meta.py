# -*- coding: utf-8 -*-

import os
import martian
import zope.component
import grokcore.view
import grokcore.component

from martian import util
from martian.error import GrokError

from zope.pagetemplate.interfaces import IPageTemplate
from zope.app.pagetemplate import ViewPageTemplateFile
from zope.publisher.interfaces.browser import IBrowserRequest

from megrok.pagetemplate.components import PageTemplate


class PageTemplateGrokker(martian.ClassGrokker):
    martian.component(PageTemplate)
    martian.directive(grokcore.component.name)
    martian.directive(grokcore.component.context)
    martian.directive(grokcore.component.provides, default=IPageTemplate)
    martian.directive(grokcore.view.layer, default=IDefaultBrowserLayer)

    def grok(self, name, factory, module_info, **kw):
        factory.module_info = module_info
        martian.ClassGrokker.grok(self, name, context, module_info, **kw)

    def execute(self, factory, config, name, context, layer, provides, **kw):

        templates = factory.module_info.getAnnotation('grok.templates', None)
        factory_name = factory.__name__.lower()
        template_name = util.class_annotation(
            factory, 'grok.template', factory_name
            )
        template = templates.get(template_name)
        
        if not template:
            raise GrokError(
                "Please define a template to use for %r." % factory,
                factory
                )
        
        if factory_name != template_name:
            if templates.get(factory_name):
                raise GrokError(
                    "Multiple possible templates for template %r. It "
                    "uses grok.template('%s'), but there is also "
                    "a template called '%s'." % (
                        factory, template_name, factory_name
                        ), factory)

        filename = template.__grok_location__
        if not os.path.exists(filename):
            raise GrokError(
                "Template %r doesn't exist." % filename,
                factory
                )
        
        pagetemplate = ViewPageTemplateFile(filename, contentType, macro)
        zope.component.provideAdapter(
            pagetemplate,
            adapts=(context, layer),
            provides=provides,
            name=name
            )
        return True
