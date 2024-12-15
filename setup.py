from setuptools import find_packages, setup
from typing import List

HYPHEN = '-e .'

def get_requirements(file_path) -> List[str]:
    '''
        This function reads the requirements.txt file and returns a list of dependencies.
    '''
    req = []
    with open(file_path) as file_obj:
        req = file_obj.readlines()
        req = [r.strip() for r in req]

        if HYPHEN in req:
            req.remove(HYPHEN)

    return req


setup(
    name='BcanD_implementation',
    version='0.0.1',
    discription = "Breast dancer detection model",
    author='Vikas Kumar Sahu, Satvika Dwaram, Harshita Pendli, Anas Anwar',
    author_email='2003vikas0906@gmail.com',
    packages=find_packages(),  # Automatically finds all packages
    install_requires=get_requirements('requirements.txt')  # Reads dependencies from requirements.txt
)
