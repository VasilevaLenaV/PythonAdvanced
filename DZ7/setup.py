from setuptools import setup, find_packages

VERSION = '0.0.1'
DESCRIPTION = 'DZ 7 создание пакетов'
LONG_DESCRIPTION = 'DZ создание пакетов создание функции и пакетов'

setup(
    name="dzutils",
    version=VERSION,
    author="lena",
    author_email="asfirs@rambler.ru",
    url="https://github.com/VasilevaLenaV",
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[],
    keywords=['python'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Education",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)