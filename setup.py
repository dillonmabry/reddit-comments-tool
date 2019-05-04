from setuptools import setup

setup(name = 'reddit_extract',
    version = '0.1.2',
    description = 'Extract reddit comments and general API helper',
    author = 'Dillon Mabry',
    author_email = 'rapid.dev.solutions@gmail.com',
    license = 'MIT',
    packages = ['reddit_extract'],
    test_suite = 'nose.collector',
    tests_require = ['nose'],
    install_requires = ['praw', 'requests'],
    include_package_data = True,
    data_files = [('', [
        'reddit_extract/resources/search_template.txt'
    ])],
    zip_safe = False)