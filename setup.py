
#!/usr/bin/env python

from distutils.core import setup

setup(name='pydbusgen',
      version='0.2beta',
      description='generates from qdbus output an python module for access',
      author='Alexander Weigl',
      author_email='alexweigl@gmail.com',
      url='http://areku.kilu.de',
      download_url='',
      scripts=['pydbusgen'],
      data_files = (
          [ ]
          )
      classifiers=[ # see http://pypi.python.org/pypi?%3Aaction=list_classifiers for all !
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        ],      
      long_description="""""",
     )
