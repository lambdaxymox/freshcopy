from setuptools import setup


config = dict(
    description = 'Fix sticky *nix file permissions by making a fresh copy.',
    author = 'Stallmanifold',
    url = 'https://github.com/stallmanifold/freshcopy',
    download_url = 'https://github.com/stallmanifold/freshcopy.git',
    author_email = 'stallmanifold@gmail.com',
    version = '0.1',
    license = "UNLICENSE",
    packages = ['freshcopy'],
    scripts = [],
    name = 'freshcopy',
    entry_points = {
        'console_scripts': [ 'freshcopy = freshcopy.freshcopy:main' ]
    }
)

setup(**config)
