from zope.configuration.config import ConfigurationMachine
from grokcore.component import zcml

def grok(module_name):
    config = ConfigurationMachine()
    zcml.do_grok('grokcore.view.meta-minimal', config)
    zcml.do_grok('megrok.pagetemplate.meta', config)
    zcml.do_grok(module_name, config)
    config.execute_actions()
