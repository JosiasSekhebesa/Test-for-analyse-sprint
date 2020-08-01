from setuptools import setup, find_packages

setup(
    name='mypackage',
    version='0.1',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Five number summary package',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/<JosiasSekhebesa>/mypackage',
    author='Josias Sekhebesa',
    author_email='1175620@students.wits.ac.za'
)