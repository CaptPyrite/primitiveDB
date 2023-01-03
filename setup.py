from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    Long_description = "\n" + fh.read()

VERSION = '0.0.2'
DESCRIPTION = 'An easy-to-use databasing library'
LONG_DESCRIPTION = 'A lightweight databasing library. to perform simple and minimalistic tasks with great and stable performance.'

setup(
    name="primitiveDB",
    version=VERSION,
    author="Fahim Ferdous (Capt.Pyrite)",
    author_email="<liveviewer360@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=Long_description,
    packages=find_packages(),
    install_requires=["Flask==2.2.2", "httpx==0.23.2", "pandas==1.5.0", "py_cpuinfo==9.0.0"],
    keywords=["python", "flask", "pandas", "database"],
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: Microsoft :: Windows",
    ]
)