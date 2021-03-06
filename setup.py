import codecs
from setuptools import setup, find_packages
import os
import re


with codecs.open(os.path.join(os.path.abspath(os.path.dirname(
        __file__)), 'aiohttp_sse', '__init__.py'), 'r', 'latin1') as fp:
    try:
        version = re.findall(r"^__version__ = '([^']+)'$", fp.read(), re.M)[0]
    except IndexError:
        raise RuntimeError('Unable to determine version.')


def read(f):
    return open(os.path.join(os.path.dirname(__file__), f)).read().strip()

install_requires = ['aiohttp>=0.14']
tests_require = install_requires + ['nose']


setup(name='aiohttp_sse',
      version=version,
      description=("Server-sent events  support for aiohttp."),
      lond_description='\n\n'.join((read('README.rst'), read('CHANGES.txt'))),
      classifiers=[
          'License :: OSI Approved :: Apache Software License',
          'Intended Audience :: Developers',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Internet :: WWW/HTTP'],
      author="Nikolay Novik",
      author_email="nickolainovik@gmail.com",
      url='https://github.com/jettify/aiohttp_sse/',
      license='Apache 2',
      packages=find_packages(),
      install_requires=install_requires,
      tests_require=tests_require,
      test_suite='nose.collector',
      include_package_data=True)
