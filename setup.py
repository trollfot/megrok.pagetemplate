# -*- coding: utf-8 -*-

import os

from setuptools import find_packages
from setuptools import setup


version = '0.8+rl0'
with open("CHANGES.rst") as f:
    changes = f.read()
with open(os.path.join("src", "megrok", "pagetemplate", "README.txt")) as f:
    readme = f.read()

setup(name='megrok.pagetemplate',
      version=version,
      description=("Page template component for Grok, "
                   "based on zope.pagetemplate"),
      long_description=u"%s\n\n%s" % (readme, changes),
      classifiers=[
          'Environment :: Web Environment',
          'Framework :: Zope3',
          'Intended Audience :: Other Audience',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Programming Language :: Python :: 3.10',
          'Programming Language :: Python :: 3.11',
      ],
      keywords='Grok Pagetemplate Zope Layout Dolmen',
      author='Souheil Chelfouh',
      author_email='trollfot@gmail.com',
      url='http://pypi.python.org/pypi/megrok.pagetemplate',
      license='GPL',
      packages=find_packages('src', exclude=['ez_setup']),
      package_dir={'': 'src'},
      namespace_packages=['megrok'],
      include_package_data=True,
      zip_safe=False,
      platforms='Any',
      extras_require={'test': [
          'zope.browserpage',
          'zope.container',
          'zope.interface',
          'zope.site',
          'zope.traversing',
          'zope.security',
          'grokcore.view >= 2.7',
      ]},
      install_requires=[
          'grokcore.component',
          'grokcore.view >= 2.2',
          'martian < 2; python_version=="2.7"',
          'setuptools',
          'zope.component >= 3.9.1',
          'zope.pagetemplate',
          'zope.publisher',
          'zope.tal < 5; python_version=="2.7"',  # transitive
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
