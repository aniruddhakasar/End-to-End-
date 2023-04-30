from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT="-e ."
def get_requirements(file_path:str)->List[str]:
    """
        This function will return the list of requiremets

    """
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace("\n","")for req in requirements]
        
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements
    
    
setup(
name="End To End",
version="0.0.1",
author="Aniruddha",
author_email="aniruddhakasar2001@gmail.com",
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
    
)