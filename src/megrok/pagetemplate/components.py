# -*- coding: utf-8 -*-

from grokcore.component import baseclass
from zope.app.pagetemplate import ViewPageTemplateFile


class PageTemplate(object):
    baseclass()

    def __call__(self, view, request):
        import pdb
        pdb.set_trace()
        return ViewPageTemplateFile


    
