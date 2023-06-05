Changelog
=========

0.8+rl1 (unreleased)
--------------------

- Nothing changed yet.


0.8+rl0 (2023-06-02)
--------------------

* Add support for Python 3.7, 3.8, 3.9, 3.10, 3.11.


0.7 (2011-01-31)
----------------

* We now use the latest changes in the ``grokcore.view`` package and
  the standalone template grokker, to avoid reimplementing the whole
  mechanism.

* Updated to be used with Grok 1.3+


0.6 (2010-11-10)
----------------

* Tested for the latest grokcore packages.

* Dependencies to ``grokcore.viewlet`` and ``zope.testing`` removed.


0.5 (2010-05-27)
----------------

* Cleaned up the code to respect the strict pep8. Removed unused imports.

* Tested for Grok 1.1


0.4.1 (2010-02-22)
------------------

* The MANIFEST has been updated so the 'templates' folder of the tests
  module is now part of the source release (thus the tests now run
  correctly).


0.4 (2010-02-21)
----------------

* Cleaned up the dependencies, to get rid of all the zope.app
  artifacts.

* Cleaned up the imports and tests.


0.3 - Beta3 Release
-------------------

* Modified tests to import all the directives needed directly from the
  package `megrok.pagetemplate` itself. [trollfot]

* Added a convenient function ``getPageTemplate`` to query the page
  template component.


0.2 - Beta2 Release
-------------------

* `megrok.pagetemplate` has been upgraded to work with the latest
  grokcore.view (1.12.1). Tests has been corrected and CodeView is
  gone. [trollfot]


0.1 - Beta1 Release
-------------------

* Initial release [trollfot]
