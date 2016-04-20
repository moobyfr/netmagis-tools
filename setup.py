from distutils.core import setup
import os

readme = os.path.join(os.path.abspath(os.path.dirname(__file__)), "README.md")
with open(readme) as fh:
    long_description = fh.read()

setup(name="netmagis-tools",
      package_dir={'netmagisclient': 'scripts/netmagisclient'},
      packages=['netmagisclient'],
      version="0.1",
      description="CLI for netmagis",
      long_description=long_description,
      author="E.Blindauer",
      author_email="e.blindauer@gmail.com",
      include_package_data=True,
      zip_safe=False,
      )
