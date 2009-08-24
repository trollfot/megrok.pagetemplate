# -*- coding: utf-8 -*-

from grokcore.component import baseclass


class PageTemplate(object):
    baseclass()

    def __call__(self, view, request):
        return self.template._template


    
