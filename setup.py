from distutils.core import setup

setup(
    name='Flask-Manage-Webpack',
    packages=['flask_manage_webpack'],
    version='0.1',
    license='MIT',
    description='Flask extension for connecting and managing webpack assets',
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
    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)
