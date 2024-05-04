from setuptools import find_packages, setup
from typing import List # type: ignore

HYPEN_E_DOT = '-e .'

def get_requirements(file_path:str)->List[str]:
    req = []
    with open(file_path) as file_obj:
        req = file_obj.readlines()
        req = [req.replace("\n","") for r in req]

        if HYPEN_E_DOT in req:
            req.remove(HYPEN_E_DOT)


setup(
name='sush_ml',
version='0.0.1',
author='sush',
author_email='sushanth.is22@bmsce.ac.in',
packages=find_packages(),
install_requires=get_requirements('req.txt')

)