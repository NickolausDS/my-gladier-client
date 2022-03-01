"""Python setup.py for my_gladier_client package"""
import io
import os
from setuptools import find_packages, setup

# single source of truth for package version
version_ns = {}
with open(os.path.join('my_gladier_client', 'version.py')) as f:
    exec(f.read(), version_ns)
version = version_ns['__version__']

install_requires = []
with open('requirements.txt') as reqs:
    for line in reqs.readlines():
        req = line.strip()
        if not req or req.startswith(('"', "#", "-", "git+")):
            continue
        install_requires.append(req)

setup(
    name='my_gladier_client',
    description='Gladier Client Template',
    url='https://github.com/NickolausDS/my-gladier-client',
    maintainer='NickolausDS',
    maintainer_email='',
    version=version_ns['__version__'],
    packages=find_packages(exclude=["tests", ".github"]),
    install_requires=install_requires,
    scripts=[],
    dependency_links=[],
)




    
    
