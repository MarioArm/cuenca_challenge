from setuptools import setup

with open('README.md', 'r') as f:
    long_description = f.read()

setup(
    name='cuenca_challenge',
    version='1.0',
    description='Cuenca challenge ',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/MarioArm/cuenca-challenge',
    author='Mario Armenta',
    author_email='mario.armenta@outlook.com',
    packages=['src'],
    install_requires=[
        'pytest>=7.1.2',
        'setuptools>=57.0.0'
    ],
)
