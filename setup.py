from setuptools import setup, find_packages
from version import __version__


def readme():
    with open('README.md') as f:
        return f.read()


def project_license():
    with open('LICENSE') as f:
        return f.read()


setup(
    name='cddcli',
    version=__version__,
    description='A command line package to enable interaction with your custom tasks platform.',
    long_description=readme(),
    author='Your Organization',
    author_email='Filip Szalewicz <fszale@gmail.com>',
    url='https://github.com/fszale/cdd-cli',
    license=project_license(),
    packages=find_packages(include=['src', 'src.cmd'], exclude=['test']),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'click',
    ],
    entry_points={
        'console_scripts': ['cddcli=src.cli:cli']
    }
)
