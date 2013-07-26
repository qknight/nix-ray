from setuptools import setup, find_packages
import os
import sys

version = '0'
shortdesc = "assistant for debugging the phases of a nix expression"
#longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

install_requires = [
    'setuptools',
    'tpv',
    'tpv.cli',
]


if sys.version_info < (2, 7):
    install_requires.append('ordereddict')
    install_requires.append('unittest2')


setup(name='nix_ray',
      version=version,
      description=shortdesc,
      #long_description=longdesc,
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Operating System :: OS Independent',
          'Programming Language :: Python',
          'Topic :: Software Development',
      ],
      keywords='',
      author='Joachim Schiele',
      author_email='js@lastlog.de',
      url='https://github.com/qknight/nix-ray',
      license='AGPLv3+',
      packages=find_packages('src'),
      package_dir={'': 'src'},
      namespace_packages=[],
      include_package_data=True,
      zip_safe=True,
      install_requires=install_requires,
      entry_points={
          # We have one command line tool: nix-ray
          'console_scripts': ['nix-ray = nix_ray:app'],

          # Subcommands for nix-ray
          'nix_ray.commands': [
              'foo = nix_ray.foo:cmd',
              'foo/baz = nix_ray.foo:baz',
              'bar = nix_ray.bar:cmd',
          ],

          # hook into xin as 'xin ray'
          'tpv.nix.xin.commands': [
              'ray = nix_ray:app',
          ],
      })
