from setuptools import setup


config = dict(
    description = 'Fix sticky *nix file permissions by making a fresh copy.',
    author = 'LambdaXymox',
    url = 'https://github.com/lambdaxymox/freshcopy',
    download_url = 'https://github.com/lambdaxymox/freshcopy.git',
    author_email = 'lambda.xymox@gmail.com',
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
