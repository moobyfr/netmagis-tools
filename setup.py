from setuptools import find_packages, setup

import os
readme = os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
with open(readme) as fh:
    long_description = fh.read()

setup(name="netmagis-tools",
      package_dir={'':'scripts'}
      version="0.1",
      description="CLI for netmagis",
      long_description=long_description,
      author="E.Blindauer",
      author_email="e.blindauer@gmail.com",
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      )

