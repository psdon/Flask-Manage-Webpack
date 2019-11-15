from setuptools import setup

import pathlib
HERE = pathlib.Path(__file__).parent

README = (HERE/"README.md").read_text()

setup(
    name='Flask-Manage-Webpack',
    packages=['flask_manage_webpack'],
    include_package_data=True,
    version='1.0.1',
    license='MIT',
    description='Flask extension for connecting and managing webpack assets',
    long_description=README,
    long_description_content_type="text/markdown",
    author='Paulo Sairel Don',
    author_email='connect.psdon@gmail.com',
    url='https://github.com/psdon/Flask-Manage-Webpack',
    keywords=['flask', 'webpack', 'manifest'],
    platforms="any",
    python_requires=">=3.6",
    install_requires=[
        'requests',
        'Flask>=1.0'
    ],
    entry_points={
        "flask.commands": [
            "manage-webpack=flask_manage_webpack.cli:init"
        ],
    },
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
    ],
)
