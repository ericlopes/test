from setuptools import setup
from package_name import metadata as m

def readme():
    with open('README.md') as f:
        return f.read()

def requirements():
    with open('requirements.txt') as r:
        return r.read().splitlines() 

setup(name=m.package,
      version=m.version,
      description=m.short_description,
      long_description=readme(),
      classifiers=[
        "Development Status :: {}".format(m.release),
        "License :: OSI Approved :: {} License".format(m.license),
        "Programming Language :: Python :: 3.3",
        "Topic :: Project :: Template",
      ],
      keywords=" ".join(m.keywords),
      url=m.url,
      author=m.author,
      author_email=m.email,
      license=m.license,
      packages=[m.package],
      install_requires=requirements(),
      include_package_data=True,
      zip_safe=False)
